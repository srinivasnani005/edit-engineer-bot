from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN: Final = "6359958863:AAHvGLbCozZzI0PlASC-NtqxFkZurgNM-Yc"
bot_username: Final = "@EditEngineerBot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to the Edit Engineer bot! I can help you search for movies and software torrents. Type '/help' for more information.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 You can type the name of the movie or software you want to search for and I will provide you with the magnet links.\nExample: 'Avengers Endgame Telugu' or 'Adobe After Effects 2024'")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛠️ This is a custom command!")




async def HandleResponse(text: str, update: Update) -> None:
    text = text.lower()

    responses = {
        'hello': "👋 Hey there, how can I assist you today?",
        'hi': "👋 Hi there! How can I help you?",
        'how are you': "😊 I'm doing well, thank you for asking! How can I help you?",
        'i love you': "❤️ Aww, that's so sweet! I'm here to assist you with anything you need!",
        'tell me a movie': "🎬 Sure! Just type the name of the movie you want to search for and I'll provide you with the magnet links!",
        "suggest some movie": "🎬 Sure! Just type the name of the movie you want to search for and I'll provide you with the magnet links!",
        'how are you doing': "😊 I'm here and ready to assist you! What do you need help with?",
        'how is everything': "🌟 Everything is going smoothly! How can I assist you today?",
        'how is it going': "👍 Everything is going great! How can I assist you today?",
        'what are you doing': "🔍 Edit Engineer is currently working on providing you with the best results. Please wait a moment!",
        'what can you do': "🤖 I can help you search for movies and software torrents. Just type the name of the movie or software you want to search for!",
        'what is your purpose': "🔍 My purpose is to assist you in finding movies and software torrents quickly and efficiently!",
        'who made you': "👨‍💻 I was created by a team of developers at Edit Engineer.",
        'where are you from': "🌍 I'm a bot living in the digital world! How can I assist you today?",
        'can you help me': "🤖 Of course! Just let me know what you need assistance with.",
        'please help me': "🤖 I'm here to help! What do you need assistance with?",
        'thank you': "🙏 You're welcome! If you need further assistance, feel free to ask.",
        'thanks': "🙏 You're welcome! Let me know if there's anything else I can help you with.",
        'good morning': "🌞 Good morning! How can I assist you today?",
        'good afternoon': "🌤️ Good afternoon! How can I assist you today?",
        'good evening': "🌆 Good evening! How can I assist you today?",
        'good night': "🌙 Good night! If you need assistance, feel free to reach out to me!",
        'bye': "👋 Goodbye! If you need help in the future, don't hesitate to ask!",
        'see you later': "👋 See you later! If you need assistance, I'll be here!",
        'take care': "👋 Take care! If you need any assistance, feel free to reach out to me!",
        'have a nice day': "🌞 Have a nice day too! If you need assistance, feel free to ask!",
        'have a great day': "🌟 Have a great day too! If you need assistance, feel free to ask!",
        'how can I help you': "🤖 You can help me by letting me know what you need assistance with!",
        'can I ask you something': "🤖 Of course! Feel free to ask me anything.",
        'what do you do': "🤖 I can help you search for movies and software torrents. Just type the name of what you're looking for!",
        'what is your name': "🤖 I'm Edit Engineer Bot! How can I assist you today?",
        'are you a human': "🤖 No, I'm a bot designed to assist you in finding movies and software torrents!",
        'are you real': "🤖 I'm as real as the assistance I provide! How can I help you today?",
        'do you sleep': "🤖 No, I'm here 24/7 to assist you whenever you need help!",
        'do you eat': "🤖 No, I don't eat. But I'm here to help you find what you're looking for!",
        'do you have feelings': "🤖 I'm just a bot, so I don't have feelings. But I'm here to assist you!",
        'do you have emotions': "🤖 No, I'm just a bot designed to assist you in finding movies and software torrents!",
        'do you have a job': "🤖 My job is to assist you in finding movies and software torrents quickly and efficiently!",
        'do you like music': "🤖 I'm just a bot, so I don't have preferences. But I'm here to help you find what you're looking for!",
        'do you like movies': "🤖 I'm just a bot, so I don't have preferences. But I can help you find movies torrents!",
        'do you like games': "🤖 I'm just a bot, so I don't have preferences. But I can help you find software torrents!",
        'do you like books': "🤖 I'm just a bot, so I don't have preferences. But I can help you find what you're looking for!",
        'do you like sports': "🤖 I'm just a bot, so I don't have preferences. But I can help you find what you're looking for!",
        'do you like art': "🤖 I'm just a bot, so I don't have preferences. But I can help you find what you're looking for!",
        'do you like technology': "🤖 I'm just a bot, so I don't have preferences. But I'm here to assist you with technology-related queries!",
        'do you like science': "🤖 I'm just a bot, so I don't have preferences. But I'm here to assist you with science-related queries!",
        'do you like history': "🤖 I'm just a bot, so I don't have preferences. But I'm here to assist you with history-related queries!",
    }

    for key, value in responses.items():
        if key in text:
            await update.message.reply_text(value)
            return

    # Default response if none of the above conditions are met
    await update.message.reply_text("🔍 Edit Engineer is working on it...")
    await update.message.reply_text("⏳ Please wait for a moment, I'm searching for the movie or software that you're looking for...")

    import requests
    api_url = "https://torrent-api-py-6rpn.onrender.com/api/v1/all/search"
    params = {"query": text}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        torrents = data.get("data", [])
        if torrents:
            # Create dictionaries to store links based on quality
            quality_links = {'2160p': [], '1080p': [], '720p': [], 'software': []}
            
            # Populate quality_links with torrents
            for torrent in torrents:
                magnet_link = torrent.get('magnet')
                if magnet_link:
                    quality = torrent.get('quality', 'N/A')
                    if quality.startswith('2160'):
                        quality_links['2160p'].append(torrent)
                    elif quality.startswith('1080'):
                        quality_links['1080p'].append(torrent)
                    elif quality.startswith('720'):
                        quality_links['720p'].append(torrent)
                    else:
                        quality_links['software'].append(torrent)
            
            # Iterate over quality_links and select top 3 links with highest seeds and peers for each quality
            for quality, links in quality_links.items():
                if quality != 'software':
                    links.sort(key=lambda x: (x.get('seeders', 0), x.get('peers', 0)), reverse=True)
                    top_links = links[:5]
                else:
                    links.sort(key=lambda x: (x.get('seeders', 0), x.get('peers', 0)), reverse=True)
                    top_links = links[:8]
                for link in top_links:
                    magnet_link = link.get('magnet')
                    message = f"🎬 <b>Movie Name:</b> {link.get('name')}\n"
                    message += f"📁 <b>File Size:</b> {link.get('size', 'N/A')}\n"
                    message += f"👥 <b>Peers:</b> {link.get('peers', 'N/A')}\n"
                    message += f"🌱 <b>Seeds:</b> {link.get('seeders', 'N/A')}\n"
                                        
                    await update.message.reply_html(message)
                                        
                    await update.message.reply_html(magnet_link)

            await update.message.reply_html("🔝🔍 The Above Links are the Highest Peers and Seeds for the Movie or Software that you are looking for...")
                                        
        else:
            await update.message.reply_text("❌ Please Check the Movie or Software that you are searching for..?")
    else:
        await update.message.reply_text("❌ Sorry, I'm unable to process your request at the moment. Please try again later.")






async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text
    await HandleResponse(text, update)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    app.add_handler(MessageHandler(filters.Text(), message_handler))  
    app.add_error_handler(error)
    app.run_polling()
