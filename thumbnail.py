import os
import re
import string
import subprocess
import traceback
from secrets import choice

import av
from PIL import Image, ImageFont, ImageDraw

# Tune these settings...
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
    return ''.join(choice(string.ascii_lowercase) for _ in range(20)) + ext


def create_thumbnail(filename: str) -> None:
    print(f'Processing: {filename}')

    jpg_name = f'{filename}.jpg'
    if os.path.exists(jpg_name):
        print('Thumbnail assumed exists!')
        return

    _, ext = os.path.splitext(filename)
    random_filename = get_random_filename(ext)
    random_filename_2 = get_random_filename(ext)
    print(f'Rename as {random_filename} to avoid decode error...')
    try:
        os.rename(filename, random_filename)
        try:
            container = av.open(random_filename)
        except UnicodeDecodeError:
            print('Metadata decode error. Try removing all the metadata...')
            subprocess.run(["ffmpeg", "-i", random_filename, "-map_metadata", "-1", "-c:v", "copy", "-c:a", "copy",
                            random_filename_2], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            container = av.open(random_filename_2)

        metadata = [
            f"File name: {filename}",
            f"Size: {container.size} bytes ({container.size / 1048576:.2f} MB)",
            f"Duration: {get_time_display(container.duration // 1000000)}",
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
        except OSError:
            print(f"Font '{FONT_NAME}' not found. Using default font.")
            font = ImageFont.load_default()
        _, min_text_height = draw.textsize("\n".join(metadata), font=font)
        image_width_per_img = int(round((IMAGE_WIDTH - PADDING) / IMAGE_PER_ROW)) - PADDING
        image_height_per_img = int(round(image_width_per_img / width * height))
        image_start_y = PADDING * 2 + min_text_height

        img = Image.new("RGB", (IMAGE_WIDTH, image_start_y + (PADDING + image_height_per_img) * IMAGE_ROWS), BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)
        draw.text((PADDING, PADDING), "\n".join(metadata), TEXT_COLOR, font=font)
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
        print('OK!')
    except Exception as e:
        traceback.print_exc()
    finally:
        try:
            container.close()
        except Exception as e:
            print("Error closing container:", e)
        os.rename(random_filename, filename)
        if os.path.exists(random_filename_2):
            os.remove(random_filename_2)


if __name__ == "__main__":
    p = input("Input the path you want to process: ")
    p = os.path.abspath(p)

    if not os.path.isdir(p):
        print(f"Path '{p}' is not a valid directory.")
        exit(1)

    for root, _, files in os.walk(p):
        print(f'Switch to root {root}...')
        os.chdir(root)
        for file in files:
            ext_regex = r"\.(mov|mp4|mpg|mpeg|flv|wmv|avi|mkv)$"
            if re.search(ext_regex, file, re.IGNORECASE):
                try:
                    create_thumbnail(file)
                except Exception as e:
                    print(f"Failed to create thumbnail for {file}: {e}")
