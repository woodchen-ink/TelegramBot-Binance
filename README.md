# Telegram Binance 价格机器人

[English](./README-EN.md)

一个简单的 Telegram 机器人,用于每小时发送来自币安的加密货币价格更新。

## 描述

这个机器人从币安获取指定加密货币对的最新价格,并每小时向指定的 Telegram 聊天发送更新。它被设计为在 Docker 容器中运行,便于部署和管理。

## 特性

- 每小时更新指定加密货币对的价格
- 可自定义要跟踪的加密货币对列表
- 在 Docker 容器中运行,便于部署
- 支持多种架构 (amd64, arm64)

## 前提条件

- Docker
- Docker Compose
- Telegram 机器人令牌
- Telegram 聊天 ID

## 快速开始

1. 克隆此仓库:
   ```
   git clone https://github.com/woodchen-ink/telegrambot-binance.git
   cd telegrambot-binance
   ```

2. 创建一个 `docker-compose.yml` 文件,内容如下:
   ```yaml
   services:
     telegrambot-binance:
       container_name: telegrambot-binance
       image: woodchen/telegrambot-binance:latest
       restart: always
       environment:
         - BOT_TOKEN=你的机器人令牌
         - CHAT_ID=你的聊天ID
         - SYMBOLS=DOGS/USDT,BTC/USDT,ETH/USDT,TON/USDT
         - TZ=Asia/Singapore
   ```

3. 将 `你的机器人令牌` 替换为你的 Telegram 机器人令牌,将 `你的聊天ID` 替换为你的 Telegram 聊天 ID。

4. 自定义 `SYMBOLS` 环境变量,设置你想要跟踪的加密货币对。

5. 运行机器人:
   ```
   docker-compose up -d
   ```

## 配置

你可以通过修改 `docker-compose.yml` 文件中的环境变量来配置机器人:

- `BOT_TOKEN`: 你的 Telegram 机器人令牌
- `CHAT_ID`: 接收更新的 Telegram 聊天 ID
- `SYMBOLS`: 要跟踪的加密货币对列表,用逗号分隔 (例如, `BTC/USDT,ETH/USDT`)
- `TZ`: 容器的时区 (默认为 Asia/Singapore)

## 从源代码构建

如果你想自己构建 Docker 镜像:

1. 克隆仓库
2. 进入项目目录
3. 构建 Docker 镜像:
   ```
   docker build -t yourusername/telegrambot-binance:latest .
   ```

## 贡献

欢迎贡献!请随时提交 Pull Request。

## 许可证

本项目采用 MIT 许可证 - 详情请见 LICENSE 文件。