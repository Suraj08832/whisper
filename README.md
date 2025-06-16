# Telegram Whisper Bot

A Telegram bot that allows users to send private whispers to other users. The bot also includes message monitoring features for groups.

## Features

- Send private whispers to users
- One-time whisper option
- Message edit detection and deletion
- Message deletion notifications
- 24/7 operation on Render

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with the following variables:
```env
BOT_TOKEN=your_bot_token
BOT_USERNAME=your_bot_username
API_ID=your_api_id
API_HASH=your_api_hash
```

4. Run the bot:
```bash
python whisper.py
```

## Deployment on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Add the following environment variables in Render dashboard:
   - BOT_TOKEN
   - BOT_USERNAME
   - API_ID
   - API_HASH

The bot will automatically deploy and run 24/7.

## Usage

1. Start the bot: `/start`
2. Send a whisper: `@your_bot_username username message`
3. Use in groups to monitor message edits and deletions

## License

MIT License 