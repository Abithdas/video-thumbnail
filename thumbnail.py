import os
import re
import subprocess
import traceback
from secrets import choice
import logging

import av
from PIL import Image, ImageFont, ImageDraw

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
IMAGE_PER_ROW = 5
IMAGE_ROWS = 7
PADDING = 5
FONT_SIZE = 16
IMAGE_WIDTH = 1536
FONT_NAME = "Helvetica.ttc"
BACKGROUND_COLOR = "#fff"
TEXT_COLOR = "#000"
TIMESTAMP_COLOR = "#fff"


def get_time_display(time: int) -> str:
    return f"{time // 3600:02d}:{time % 3600 // 60:02d}:{time % 60:02d}"


def get_random_filename(ext: str) -> str:
    return ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(20)) + ext


def format_size(size: int) -> str:
    if size < 1024**3:  # Less than 1 GB
        return f"{size / 1024**2:.2f} MB"
    else:
        return f"{size / 1024**3:.2f} GB"


def create_thumbnail(filename: str) -> None:
    try:
        logging.info(f'Processing: {filename}')

        jpg_name = f'{filename}.jpg'
        if os.path.exists(jpg_name):
            logging.info('Thumbnail already exists!')
            return

        _, ext = os.path.splitext(filename)
        random_filename = get_random_filename(ext)
        random_filename_2 = get_random_filename(ext)
        logging.info(f'Renaming {filename} to {random_filename} to avoid decode error...')
        os.rename(filename, random_filename)
        
        try:
            container = av.open(random_filename)
        except av.AVError:
            logging.error('AVError: Metadata decode error. Trying to remove all metadata...')
            subprocess.run(["ffmpeg", "-i", random_filename, "-map_metadata", "-1", "-c:v", "copy", "-c:a", "copy", random_filename_2], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            container = av.open(random_filename_2)

        # Get file size
        size_bytes = os.path.getsize(random_filename)
        size_formatted = format_size(size_bytes)

        metadata = [
            f"File name: {filename}",
            f"Size: {size_formatted}",
            f"Duration: {get_time_display(container.duration // 1000000)}",
            f"Frame width: {container.streams.video[0].width}",
            f"Frame height: {container.streams.video[0].height}",
            f"Bit rate: {container.bit_rate // 1024} kbps",
        ]

        start = min(container.duration // (IMAGE_PER_ROW * IMAGE_ROWS), 5 * 1000000)
        end = container.duration - start
        time_marks = [
            start + (end - start) // (IMAGE_ROWS * IMAGE_PER_ROW - 1) * i
            for i in range(IMAGE_ROWS * IMAGE_PER_ROW)
        ]

        images = []
        for mark in time_marks:
            container.seek(mark)
            for frame in container.decode(video=0):
                images.append((frame.to_image(), mark // 1000000))
                break

        width, height = images[0][0].width, images[0][0].height
        metadata.append(f'Video: ({width}px, {height}px), {container.bit_rate // 1024}kbps')

        img = Image.new("RGB", (IMAGE_WIDTH, IMAGE_WIDTH), BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype(FONT_NAME, FONT_SIZE)
        except (OSError, IOError) as e:
            logging.warning(f"Font '{FONT_NAME}' not found or could not be loaded. Using default font.")
            font = ImageFont.load_default()

        text = "\n".join(metadata)
        text_bbox = draw.textbbox((PADDING, PADDING), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        draw.text((PADDING, PADDING), text, TEXT_COLOR, font=font)

        image_width_per_img = int(round((IMAGE_WIDTH - PADDING) / IMAGE_PER_ROW)) - PADDING
        image_height_per_img = int(round(image_width_per_img / width * height))
        image_start_y = PADDING * 2 + text_height

        img = Image.new("RGB", (IMAGE_WIDTH, image_start_y + (PADDING + image_height_per_img) * IMAGE_ROWS), BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)
        draw.text((PADDING, PADDING), text, TEXT_COLOR, font=font)

        for idx, snippet in enumerate(images):
            y = idx // IMAGE_PER_ROW
            x = idx % IMAGE_PER_ROW
            new_img, timestamp = snippet
            new_img = new_img.resize((image_width_per_img, image_height_per_img), resample=Image.BILINEAR)
            x = PADDING + (PADDING + image_width_per_img) * x
            y = image_start_y + (PADDING + image_height_per_img) * y
            img.paste(new_img, box=(x, y))
            draw.text((x + PADDING, y + PADDING), get_time_display(timestamp), TIMESTAMP_COLOR, font=font)

        img.save(jpg_name)
        logging.info(f'Thumbnail saved: {jpg_name}')

    except Exception as e:
        logging.error(f'Error processing {filename}: {e}')
        traceback.print_exc()

    finally:
        try:
            container.close()
        except Exception as e:
            logging.error("Error closing container:", e)
        
        try:
            os.rename(random_filename, filename)
        except Exception as e:
            logging.error(f"Error renaming {random_filename} back to {filename}: {e}")

        if os.path.exists(random_filename_2):
            try:
                os.remove(random_filename_2)
            except Exception as e:
                logging.error(f"Error deleting {random_filename_2}: {e}")


if __name__ == "__main__":
    p = input("Input the path you want to process: ").strip()
    p = os.path.abspath(p)

    if not os.path.isdir(p):
        logging.error(f"Path '{p}' is not a valid directory.")
        exit(1)

    for root, _, files in os.walk(p):
        logging.info(f'Switch to root {root}...')
        os.chdir(root)
        for file in files:
            ext_regex = r"\.(mov|mp4|mpg|mpeg|flv|wmv|avi|mkv)$"
            if re.search(ext_regex, file, re.IGNORECASE):
                create_thumbnail(file)
