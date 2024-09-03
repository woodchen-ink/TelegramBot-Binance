# Telegram Binance Price Bot

A simple Telegram bot that sends hourly updates of cryptocurrency prices from Binance.

## Description

This bot fetches the latest prices for specified cryptocurrency pairs from Binance and sends hourly updates to a designated Telegram chat. It's designed to run in a Docker container for easy deployment and management.

## Features

- Hourly price updates for specified cryptocurrency pairs
- Customizable list of cryptocurrency pairs to track
- Runs in a Docker container for easy deployment
- Supports multiple architectures (amd64, arm64)

## Prerequisites

- Docker
- Docker Compose
- Telegram Bot Token
- Telegram Chat ID

## Quick Start

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/telegrambot-binance.git
   cd telegrambot-binance
   ```

2. Create a `docker-compose.yml` file with the following content:
   ```yaml
   services:
     telegrambot-binance:
       container_name: telegrambot-binance
       image: woodchen/telegrambot-binance:latest
       restart: always
       environment:
         - BOT_TOKEN=your_bot_token_here
         - CHAT_ID=your_chat_id_here
         - SYMBOLS=DOGS/USDT,BTC/USDT,ETH/USDT,TON/USDT
         - TZ=Asia/Singapore
   ```

3. Replace `your_bot_token_here` with your Telegram Bot Token and `your_chat_id_here` with your Telegram Chat ID.

4. Customize the `SYMBOLS` environment variable with the cryptocurrency pairs you want to track.

5. Run the bot:
   ```
   docker-compose up -d
   ```

## Configuration

You can configure the bot by modifying the environment variables in the `docker-compose.yml` file:

- `BOT_TOKEN`: Your Telegram Bot Token
- `CHAT_ID`: The Telegram Chat ID where updates will be sent
- `SYMBOLS`: Comma-separated list of cryptocurrency pairs to track (e.g., `BTC/USDT,ETH/USDT`)
- `TZ`: Timezone for the container (default is Asia/Singapore)

## Building from Source

If you want to build the Docker image yourself:

1. Clone the repository
2. Navigate to the project directory
3. Build the Docker image:
   ```
   docker build -t yourusername/telegrambot-binance:latest .
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.