from pyrogram import Client, filters
from pyrogram.types import Message
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize the bot (using the same instance from whisper.py)
from whisper import app

@app.on_edited_message(filters.group)
async def handle_edited_message(client, message: Message):
    try:
        # Get the original message
        original_text = message.text or message.caption or "No text content"
        
        # Delete the edited message
        await message.delete()
        
        # Notify the group
        notification = f"⚠️ **Message Edit Detected**\n\n" \
                      f"**User:** {message.from_user.mention}\n" \
                      f"**Original Message:** {original_text}\n\n" \
                      f"*The edited message has been deleted.*"
        
        await message.reply_text(notification)
        logger.info(f"Edited message deleted from user {message.from_user.id}")
        
    except Exception as e:
        logger.error(f"Error handling edited message: {e}")

@app.on_deleted_messages(filters.group)
async def handle_deleted_message(client, messages):
    try:
        for message in messages:
            if message.from_user:
                notification = f"⚠️ **Message Deletion Detected**\n\n" \
                             f"**User:** {message.from_user.mention}\n" \
                             f"**Message Content:** {message.text or message.caption or 'No text content'}\n\n" \
                             f"*The message has been deleted.*"
                
                await message.reply_text(notification)
                logger.info(f"Deleted message notification sent for user {message.from_user.id}")
                
    except Exception as e:
        logger.error(f"Error handling deleted message: {e}")

# Start the bot with error handling
if __name__ == "__main__":
    try:
        logger.info("Starting message handler...")
        app.run()
    except KeyboardInterrupt:
        logger.info("Message handler stopped by user")
    except Exception as e:
        logger.error(f"Failed to start message handler: {e}") 