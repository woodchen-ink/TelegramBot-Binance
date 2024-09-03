import os
import ccxt
import telebot
import schedule
import time
from datetime import datetime, timedelta
import pytz

# 设置时区
singapore_tz = pytz.timezone('Asia/Singapore')

# 交易所设置
exchange = ccxt.binance()

# Telegram Bot 设置
BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']
bot = telebot.TeleBot(BOT_TOKEN)

# 获取币种列表
SYMBOLS = os.environ['SYMBOLS'].split(',')

def get_price(symbol):
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

def send_price_update():
    now = datetime.now(singapore_tz)
    message = f"当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')} (SGT)\n价格:\n"
    for symbol in SYMBOLS:
        price = get_price(symbol)
        message += f"{symbol}: ${price:.4f}\n"
    bot.send_message(CHAT_ID, message)

# 立即执行一次价格更新
print("Sending initial price update...")
send_price_update()

# 设置定时任务，每小时整点执行
for hour in range(24):
    schedule.every().day.at(f"{hour:02d}:00").do(send_price_update)

print("Scheduled tasks set. Waiting for next hour...")

# 等待下一个整点
now = datetime.now(singapore_tz)
next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
time.sleep((next_hour - now).total_seconds())

print("Starting main loop...")

while True:
    schedule.run_pending()
    time.sleep(30)  # 每30秒检查一次，可以根据需要调整
