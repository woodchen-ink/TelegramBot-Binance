FROM python:3.9-slim

# 设置时区
ENV TZ=Asia/Singapore
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY price_bot.py .

CMD ["python", "price_bot.py"]
