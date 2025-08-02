# Telegram File Cleaner Bot

Send a `.sh` file to this bot, and it will return a cleaned `.txt` file with only file names and URLs.

## Features
- Extracts only valid file names (like .pdf, .zip, .mp4, etc.)
- Extracts all valid URLs
- Returns a cleaned text file

## How to Run Locally
1. Replace your bot token in `main.py`
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the bot:
    ```
    python main.py
    ```

## Deploy to Render
Make sure you include:
- `main.py`
- `requirements.txt`
- `Procfile`
- `.gitignore`

Then connect your GitHub repo to [Render](https://render.com/) and deploy!
