# Archive X — Consolidated GitHub Research Shortlist
Verified: 2026-10-09

## Purpose
Research repositories relevant to Telegram ingestion, Telegram-backed storage, searchable media libraries, thumbnails, streaming/playback, metadata, and UI testing. Use these projects to study architectures and test strategies—not to copy code wholesale.

## Verification notes
- All 15 newly requested repositories were resolved through GitHub's repository API and are public and not marked archived as of 2026-10-09.
- README content, repository metadata, and latest-commit timestamps were inspected where available.
- A repository being public and not archived does not prove it is secure, production-ready, well-tested, or actively maintained. Check licenses, open issues, dependencies, release provenance, and Windows/browser compatibility before adoption.
- Several repositories have old last-push dates; treat them as research references until compatibility and security are reviewed.

## 1. First-priority repositories

1. **NoBuf** — https://github.com/Istiaq-Edu/NoBuf  
   Desktop Telegram video library focused on near-instant progressive playback, continuous prebuffering, and seeking. Relevant to playback latency, seeking, media discovery, and thumbnail/loading states. README describes Windows, macOS, and Linux support. Latest push checked: 2026-09-26; MIT license reported.

2. **Telegram Drive** — https://github.com/caamer20/Telegram-Drive  
   Local-first workspace using a user's Telegram Saved Messages and channels; supports organizing, transferring, previewing, streaming, syncing, and sharing. Strong reference for desktop library UX, Telegram storage references, and cross-platform architecture. Latest push: 2026-10-05. GitHub did not report a recognized license identifier; verify the license file before reuse.

3. **TGWebDrive** — https://github.com/Sam8r/TGWebDrive  
   Self-hosted web drive using Telegram as storage, with folders, sharing, multi-user support, REST API, thumbnails, previews, and seekable HTTP-range streaming. Relevant to web library, file resolver, range requests, sharing, and responsive UI. Latest push: 2026-08-08; MIT license reported.

4. **TelePlay** — https://github.com/subinps/TelePlay  
   Telegram-backed media server with web and Android/TV clients and on-demand streaming using parallel downloads. Study multi-client playback, server/client separation, media organization, and streaming. Latest push: 2026-07-16; MIT license reported.

5. **tgstreamer** — https://github.com/xqube/tgstreamer  
   Telegram bot exposing HTTP stream/download URLs, including Range-request seeking and stream limits. Useful for streaming endpoints, access control, concurrency limits, and player compatibility. Latest push: 2025-12-27; verify licensing before reuse.

6. **Telegram Media Downloader (botnick)** — https://github.com/botnick/telegram-media-downloader  
   Self-hosted downloader and web dashboard for channel/group media and chat backups using a Telegram user account. README describes backfill, queues, retry/cancel, deduplication, sharing, and library views. Useful for ingestion, checkpoint/resume, progress reporting, and media catalog UI. Latest push: 2026-10-02; MIT license reported.

## 2. Additional newly requested repositories

7. **FastStream** — https://github.com/Andrews54757/FastStream  
   Browser extension/player for MP4, HLS, and DASH with prebuffering, parallel requests, subtitles, and playback controls. A browser playback/accessibility reference, not a Telegram ingestion backend. Latest push: 2026-10-09. GitHub returned NOASSERTION for license; verify licensing before reuse.

8. **Telegramedia** — https://github.com/kernoeb/telegramedia  
   Android player built with TDLib and libmpv that progressively streams video/audio, supports offline downloads, subtitles, playback resume, and a unified library across selected chats. Useful for player lifecycle, progressive streaming, and media-source browsing. Latest push: 2026-07-11; GPL-3.0 reported.

9. **tg-archiver** — https://github.com/osintukraine/tg-archiver  
   Self-hosted Telegram channel archiver with media storage, backfill, real-time monitoring, full-text search, translation, RSS feeds, and SHA-256 deduplication. Useful for ingestion completeness, durable archives, metadata search, and duplicate handling. Latest push: 2026-01-04; AGPL-3.0 reported.

10. **telegram-archiver** — https://github.com/roverx12345/telegram-archiver  
    Archives forwarded media, Saved Messages, and configured channels to local storage/NAS, with deduplication, retry, and restart recovery. Relevant to resilient download jobs and crash recovery. Latest push: 2026-07-09; MIT license reported.

11. **mediadock** — https://github.com/kalyanpawar/mediadock  
    Python automation downloads from Telegram and qBittorrent, organizes files into a Jellyfin-compatible library, identifies media from filenames, avoids duplicate processing, and refreshes Jellyfin. Useful for post-ingestion organization and media-server integration. Latest push: 2026-08-01; MIT license reported. Small, early-stage repository; inspect implementation and tests carefully.

12. **DownloadBot** — https://github.com/gaowanliang/DownloadBot  
    Go-based Telegram bot for controlling aria2, managing server files, and transferring files to cloud providers such as OneDrive and Google Drive. Reference for queues/status and transfer orchestration rather than a complete searchable library. Latest push: 2023-02-16; Apache-2.0 reported. Treat as a legacy reference pending compatibility review.

13. **aria-telegram-mirror-bot** — https://github.com/out386/aria-telegram-mirror-bot  
    Uses aria2 for HTTP(S)/BitTorrent downloads and uploads results to Google Drive, with queueing and parallel downloads. Useful for job queues and transfer orchestration, less for channel indexing. Latest push: 2021-01-03; MIT license reported. Legacy reference pending dependency/security review.

14. **tclone_bot** — https://github.com/fuara/tclone_bot  
    Rclone-based bot for moving files between Telegram and remote cloud storage, with batch transfers, archive extraction/creation, dedupe, and file management. Useful for transfer workflows, not a direct library-indexing solution. Latest push: 2022-09-20; GPL-3.0 reported. Legacy reference pending dependency review.

15. **arr-stack** — https://github.com/ahbanavi/arr-stack  
    Docker-based media automation stack using Sonarr/Radarr/Prowlarr/Bazarr, aria2, tinyMediaManager, and Jellyfin. Useful for downstream organization, metadata/artwork ownership, rescan/reconciliation, and container integrations; not Telegram-first. Latest push: 2026-10-05; MIT license reported.

## 3. Existing shortlist (retain)

### Telegram ingestion / client integration
- telegram_media_downloader — https://github.com/Dineshkarthik/telegram_media_downloader
- TDLib — https://github.com/tdlib/td
- Telethon — https://github.com/LonamiWebs/Telethon (archived when previously checked; legacy reference)
- Pyrogram — https://github.com/pyrogram/pyrogram (archived when previously checked; legacy reference)
- aiogram — https://github.com/aiogram/aiogram

Note: The existing Dineshkarthik downloader and the newly added botnick/telegram-media-downloader are different projects.

### Library indexing and metadata
- Jellyfin — https://github.com/jellyfin/jellyfin
- Navidrome — https://github.com/navidrome/navidrome
- PhotoPrism — https://github.com/photoprism/photoprism
- Stash — https://github.com/stashapp/stash
- Jellyfin Web — https://github.com/jellyfin/jellyfin-web

### Thumbnails and image processing
- FFmpeg — https://github.com/FFmpeg/FFmpeg
- Thumbor — https://github.com/thumbor/thumbor
- Smartcrop — https://github.com/muesli/smartcrop

### Playback and browser testing
- hls.js — https://github.com/video-dev/hls.js
- dash.js — https://github.com/Dash-Industry-Forum/dash.js
- Shaka Player — https://github.com/shaka-project/shaka-player
- Playwright — https://github.com/microsoft/playwright
- Playwright Python — https://github.com/microsoft/playwright-python

### Other Telegram storage / file delivery references
- Surf-TG — https://github.com/weebzone/Surf-TG
- Pentaract — https://github.com/Dominux/Pentaract
- TG-FileStreamBot — https://github.com/anasty17/TG-FileStreamBot
- telegram-cloud-drive (victormanuel8414) — https://github.com/victormanuel8414/telegram-cloud-drive
- File Sharing Bot — https://github.com/CodeXBotz/File-Sharing-Bot
- Rclone Mirror-Leech Telegram Bot — https://github.com/Sam-Max/rcmltb
- TorToolkit-Telegram — https://github.com/yash-dk/TorToolkit-Telegram
- telegram-cloud-drive (huydatvn) — https://github.com/huydatvn/telegram-cloud-drive

## 4. Archive X bug-to-repository mapping

- **Missing snapshots, broken thumbnail cards, absent timeline previews:** NoBuf, Telegram Drive, TGWebDrive, FFmpeg, Thumbor, Smartcrop. Investigate a canonical asset resolver, snapshot readiness, cache invalidation, and consistent paths across UI surfaces.
- **Library stalls around 400 videos / incomplete channel scans:** Telegram Media Downloader (botnick), tg-archiver, telegram-archiver, Surf-TG, PhotoPrism, Jellyfin. Inspect pagination, per-channel cursors, hard-coded caps, resumability, and discovered-versus-persisted-versus-rendered counts.
- **Slow startup, buffering, or freeze after repeated seeks:** NoBuf, TGWebDrive, TelePlay, tgstreamer, Telegramedia, FastStream, hls.js, dash.js, Shaka Player, FFmpeg. For MP4, test HTTP Range responses, container metadata, stale seek requests, active-player ownership, retries, and read-ahead.
- **Wrong performer/video metadata:** Stash, Jellyfin, Jellyfin Web. Treat filename similarity as evidence, use confidence thresholds, and allow human review of ambiguous matches.
- **Scan says 100% despite missing assets:** Telegram Media Downloader (botnick), tg-archiver, telegram-archiver, PhotoPrism, Jellyfin. Track discovered, processed, failed, skipped, pending, and verified-complete counts separately.
- **Channel artwork/profile-image sync:** Jellyfin Web, Stash, Telegram Drive. Use a canonical image record and explicit sync/cache status.
- **Duplicate movement between Telegram channels:** Telegram Drive, TGWebDrive, Pentaract. Verify destination metadata before removing source associations; make moves recoverable and auditable.
- **Cross-device / responsive browsing:** Telegram Drive, TGWebDrive, TelePlay, Jellyfin Web, Playwright. Test small mobile viewports, portrait/landscape, desktop, and ultrawide screens.
- **Media organization after download:** mediadock, arr-stack, Jellyfin. Define one owner for filenames/metadata/artwork and reconcile external library indexes after movement.

## 5. Recommended review order

1. NoBuf — playback, prebuffering, seeking, thumbnail/loading behavior.
2. Telegram Drive — broad Telegram-backed workspace and cross-platform UX.
3. TGWebDrive — web library, range streaming, thumbnails, folders, sharing, REST API.
4. Telegram Media Downloader (botnick) — ingestion, backfill, job tracking, deduplication, dashboard.
5. TelePlay — streaming architecture and multiple client surfaces.
6. tgstreamer — direct stream endpoint, range requests, concurrency, authorization.
7. tg-archiver and telegram-archiver — scan durability, archiving, search, restart recovery.
8. Telegramedia and FastStream — playback/player behavior and browser/mobile ideas.
9. mediadock and arr-stack — post-ingestion organization and metadata reconciliation.
10. Pentaract, Surf-TG, TG-FileStreamBot, plus existing indexing/thumbnail/testing tools — compare specific design choices.

## 6. Implementation priority

### P0 — scan integrity
- Reproduce and fix the ~400-video truncation issue.
- Use per-channel checkpoints, resumable/idempotent jobs, bounded retries, and API-rate-limit handling.
- Show discovered, processed, failed, skipped, pending, and verified-complete counts separately.
- Never mark a scan 100% until expected enumeration and persistence are verified.
- Never reconcile/delete library entries based on an incomplete scan.

### P1 — playback and thumbnails
- Build one canonical snapshot/storyboard resolver for every UI surface.
- Prefer existing snapshots; use storyboards only when snapshots are unavailable.
- Test HTTP Range behavior, MP4 metadata, first-frame latency, repeated seeks, stale requests, and next-video startup.
- Instrument thumbnail states as queued, ready, unavailable, and failed.

### P2 — identity and performance
- Use confidence thresholds and human review for ambiguous performer/studio matches.
- Measure first-frame time, seek-resume time, stalls, and thumbnail-generation errors.
- Optimize after correctness and telemetry are established.

### P3 — curation and compatibility
- Make cross-channel moves transactional/recoverable, with duplicate checks and audit trail.
- Add fallback artwork and profile-image editing/sync states.
- Reuse bulk metadata editing in Performer/Studio UI.
- Run responsive and cross-browser tests; separately verify native Windows + Google Chrome.

## 7. Adoption checklist
- Confirm maintenance, recent commits/releases, open security issues, and known bugs.
- Read and comply with the license; repositories with NOASSERTION or no recognized license need explicit license-file review.
- Run tests, dependency/security scans, and inspect transitive dependencies/build provenance.
- Confirm API/session model, permissions, channel history access, media delivery, and platform requirements.
- Respect Telegram API limits, privacy, access permissions, and applicable terms.
- Test with a small controlled dataset before pointing Archive X at the full library.
