import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ))
API_HASH = getenv("API_HASH", )

BOT_TOKEN = getenv("BOT_TOKEN", )

MONGO_DB_URI = getenv("MONGO_DB_URI", )
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "˹ 𝐑𝐀𝐍𝐉𝐇𝐀🕊️⃝🦋𝐌𝐔𝐒𝐈𝐂♪˼")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5635825262").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Raichuop07/RANJHA")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Ranjhaoffical")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Ranjhamusicsupport")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "701c43b1f97849a3ab0012473f889558")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "10dc41fb33414ab2b56eaf7023d613c1")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQAbCHCx3cExZR79W9CCwYcosSD_5XvsRQG2x8fxqIprr32hHJMZU_eLvZe2t1ZAE4k4YW_e_E9tpbVbr0EUtBkS6xps7gTJZEuKftR9dQdfYP8E_KUhB-YocSjILpysMP4f1BREbNsau_G6mod75HWoy9hFf7uOsCXyZgfrFfu5oJ-L1rZYMm3HC071FoBvIETug0p1JgSl8YLp6wtB4RtHhAfm8yQ2xE86iCFrWIoQWw-WUcLKUbjpJ9oiDFHmVGHkE1kTNrziEJ_6lq-YVPtxRBlWQuD9fB18xlJKjK95Ni8JmAINUTf7OedWI-nPV_LZ8YTB8ahCFqHlztv9f3PPAAAAAWuiZ3YA")
STRING2 = getenv("STRING_SESSION2", "BQBCSmSEBHZRZ_Rlrz5Qj3klDlOhBhO0dOvqpFyt4t1Fjv3WtTpSgR4HbU9BBHLyPDcgvH_X7_C0wTLCsW44QvTxAvhjiq4ZNLaCq5vkCKflnI_flyuYiyBwFU9EyzNeYvduKMOxwgNNSQjImAD-G_YikwXwpXb-l3UgRFfgb5lozKCCuCE7PDeux0Z9wMiCwKHJvJko__Sv3Ay5jSYgdf8PKKaCkPf9dggRUgzFEBx1CCCo3Pu3oa-yZYzWbHhfs1oPOggUfMBiBsg6g_xtTcY26QacCMbChN-0I-e4qAdqQNa9zFNEzjp3SDa2UmKLDxCtHMkvm81Fm2_1aU7t-PrXAAAAAWHqu1UA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/e5b19d1a4786342f69d30.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/d495fd15404e41dacf2e9.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/d495fd15404e41dacf2e9.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/e5b19d1a4786342f69d30.jpg"
