import telebot
import re

TOKEN = "8210418363:AAHnzs0HuGH-pwrC_JWup1Vcda50kuOXD60"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "📂 Send me a .sh file and I will clean it to only show file names and URLs.")

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    input_path = "input.sh"
    output_path = "output.txt"

    with open(input_path, "wb") as f:
        f.write(downloaded_file)

    clean_txt(input_path, output_path)

    with open(output_path, "rb") as f:
        bot.send_document(message.chat.id, f)

def clean_txt(input_file, output_file):
    url_pattern = re.compile(r'https?://[^\s\'"]+')
    file_name_pattern = re.compile(r'[\w\-.]+\.(pdf|zip|rar|txt|jpg|png|mp4)', re.IGNORECASE)

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    for line in lines:
        if url_pattern.search(line) or file_name_pattern.search(line):
            result.append(line.strip())

    with open(output_file, 'w', encoding='utf-8') as f:
        for line in result:
            f.write(line + '\n')

bot.infinity_polling()
