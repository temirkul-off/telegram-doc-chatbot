from dotenv import load_dotenv, dotenv_values
load_dotenv()

from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    filters
)
from qa_pipeline import conv_chain, db

TOKEN = dotenv_values().get("TOKEN")
user_chains = {}

async def handle_message(update, ctx):
    chat_id = update.effective_chat.id
    user_q  = update.message.text

    if chat_id not in user_chains:
        import copy
        user_chains[chat_id] = copy.deepcopy(conv_chain)

    chain = user_chains[chat_id]

    hits = chain.retriever.get_relevant_documents(user_q)
    if not hits:
        return await update.message.reply_text(
            "❓ Sorry, I don't know about that. I can only answer from the document."
        )

    result = chain.invoke({"question": user_q})
    answer = result["answer"]

    print(f"[chat_id={chat_id!r}] ❯ User asked: {user_q!r}")
    print(f"[chat_id={chat_id!r}] ❮ Bot answered: {answer!r}")
    
    await update.message.reply_text(answer)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )
    print("Bot is running…")
    app.run_polling()