

# Discord AI Bot

This Discord bot uses Google Generative AI and Replicate AI to generate text and images based on user prompts.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project directory and add your Discord bot token and Google API key:
   ```
   DISCORD_TOKEN=your_discord_token_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```
4. Run the bot script:
   ```
   python bot.py
   ```

## Usage

### Text Generation

To generate text, use the `/chat` command followed by your prompt. For example:
```
/chat Tell me a joke.
```

### Image Generation

To generate images, use the `/image` command followed by your prompt. For example:
```
/image Landscape with mountains and rivers.
```

## Dependencies

- discord.py: Python wrapper for the Discord API.
- dotenv: Library for loading environment variables from a `.env` file.
- replicate: Python package for interacting with the Replicate AI API.
- google.generativeai: Python package for interacting with the Google Generative AI API.

## Credits

- [Discord.py](https://github.com/Rapptz/discord.py)
- [dotenv](https://github.com/theskumar/python-dotenv)
- [Replicate AI](https://replicate.ai/)
- [Google Generative AI](https://github.com/google-research/google-research/tree/master/generative_aim)