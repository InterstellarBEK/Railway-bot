# ─── Bot sozlamalari ──────────────────────────────────────────────────────────

# Token Railway Variables dan o'qiladi (xavfsiz usul)
import os
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# Ma'lumotlar bazasi fayli
DB_PATH = "monitors.db"

# Tekshirish intervali (soniyalarda) — 5 daqiqa
CHECK_INTERVAL = 5 * 60

# Bir foydalanuvchi uchun maksimal faol kuzatuvlar soni
MAX_MONITORS_PER_USER = 5
