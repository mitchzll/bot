# Discord Bot Project

This project is a simple Discord bot built using Python. It utilizes the `discord.py` library to interact with the Discord API and provides a modular structure through the use of cogs.

## Project Structure

```
discord-bot
├── src
│   ├── bot.py
│   ├── cogs
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd discord-bot
   ```

2. **Install dependencies:**
   Make sure you have Python 3.8 or higher installed. Then, run:
   ```
   pip install -r requirements.txt
   ```

3. **Create a Discord bot application:**
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application and add a bot to it.
   - Copy the bot token and replace it in the `bot.py` file.

4. **Run the bot:**
   ```
   python src/bot.py
   ```

## Usage

Once the bot is running, you can interact with it in your Discord server. You can add commands and cogs to extend its functionality.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the bot.