# Discord_music_bot


บอท Discord เปิดเพลงด้วย Python โดยใช้ [discord.py](https://discordpy.readthedocs.io/) + [Wavelink](https://wavelink.readthedocs.io) พร้อมเชื่อมต่อ [Lavalink](https://github.com/freyacodes/Lavalink) เพื่อให้เสียงลื่นไหล ไม่กระตุก

---

## 📌 ฟีเจอร์
- ✅ เล่นเพลงจาก YouTube ได้ (ผ่าน Lavalink)
- ✅ รองรับคำสั่งพื้นฐาน: `!play`, `!pause`, `!resume`, `!stop`
- ✅ ใช้งานได้หลาย Voice Channels พร้อมกัน
- ✅ สร้างบน Ubuntu Server หรือเครื่อง Windows ก็ได้

---

## ⚙️ ขั้นตอนการติดตั้ง (บน Ubuntu Server)

### 1. ติดตั้ง Dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install openjdk-17-jre ffmpeg python3 python3-pip tmux -y
```

---

### 2. ติดตั้งและรัน Lavalink

```bash
mkdir ~/lavalink && cd ~/lavalink
wget https://github.com/freyacodes/Lavalink/releases/latest/download/Lavalink.jar
nano application.yml
```

> วาง config นี้ใน `application.yml`:

```yaml
server:
  port: 2333
  address: 0.0.0.0

lavalink:
  server:
    password: "youshallnotpass"
    sources:
      youtube: true
      soundcloud: true
    bufferDurationMs: 400
```

> รัน Lavalink:

```bash
java -jar Lavalink.jar
```

(หรือใช้ `tmux` เพื่อเปิด background)

---

### 3. ติดตั้งและรัน Python Bot

```bash
mkdir ~/musicbot && cd ~/musicbot
# ใส่ไฟล์ bot.py ที่อยู่ใน repo นี้
pip3 install -U discord.py wavelink
```

เปิดไฟล์ `bot.py` และใส่ token:

```python
bot.run("YOUR_DISCORD_BOT_TOKEN")
```

จากนั้นรัน:

```bash
python3 bot.py
```

---

## 🎮 วิธีใช้งานใน Discord

เข้าร่วม voice แล้วใช้คำสั่ง:

- `!play ชื่อเพลง` — ค้นหาและเล่นจาก YouTube
- `!pause` — หยุดชั่วคราว
- `!resume` — เล่นต่อ
- `!stop` — หยุดและออกจาก voice

---

## 🧪 ตัวอย่าง

```
!play Numb Linkin Park
!pause
!resume
!stop
```

---

## 💡 หมายเหตุ
- ต้องใช้ **Java 11+** สำหรับรัน Lavalink
- ถ้าใช้บน Windows ก็ทำได้เหมือนกัน
- รองรับการขยายคำสั่ง เช่น `skip`, `queue`, `volume`, `loop`

---

## 🌐 Credits

- [discord.py](https://discordpy.readthedocs.io/)
- [wavelink](https://wavelink.readthedocs.io)
- [Lavalink](https://github.com/freyacodes/Lavalink)

---
