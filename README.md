# Telegram Document-Grounded Chatbot

A free, open-source Telegram chatbot that answers **only** from a specified Google Doc, built with:

- 🐍 **Python 3.8+**
- 📚 **LangChain** + **FAISS** for retrieval
- 🤗 **Sentence-Transformers** & **HuggingFace Transformers** for embeddings & generation
- 📲 **python-telegram-bot** for bot integration
- 🔒 Memory isolation per-chat via **ConversationalRetrievalChain**

---

## 🚀 Features

- **Document-only answers**: refuses any out-of-scope questions
- **Original document**: 
- **Conversational memory**: carries context turn-to-turn per user
- **Free & local**: no paid APIs; run everything on your own hardware

## 📦 Installation

1. **Clone the repo**:
```bash
   git clone https://github.com/yourusername/telegram-doc-chatbot.git
   cd telegram-doc-chatbot
```
2. **Create & activate a venv**:
```bash
   python -m venv .venv
   source .venv/bin/activate       # Linux/Mac  
   .venv\Scripts\activate          # Windows PowerShell
```
3. **Install dependencies**:
```bash
   pip install -r requirements.txt
```
4. **Set up your environment**:
- Create .env file in the root of your project
- Add the `TOKEN` variable and store your telegram bot token there

## ⚙️ Usage

1. **Embed your docs (only first run or when data changes):**
```bash
   python embed.py

```
2. **Start the bot:**
```bash
   python bot.py
```

## 🏗 Architecture

1. **Data preparation**:
- I downloaded the main document and doc-files inside as .txt format.
- I cleaned them up from grammar mistakes, unneccessary info, structured better and merged them all together into the single `main_doc.txt` file.
2. **Data ingestion**
- `embed.py` reads the `main_doc.txt` data file, chunks it, embeds with Sentence-Transformers, and stores vectors in FAISS.
3. **Retrieval-augmented generation**
- `qa_pipeline.py` loads FAISS + a local LLM (e.g. Flan-T5-base).
- Builds a ConversationalRetrievalChain with per-chat memory.
4. **Telegram integration**
- `bot.py` listens for messages, checks “in scope” with a quick FAISS similarity search, invokes the chain, logs the Q&A, and replies.

## ⚠️ Limitations
- Locally hosted LLMs may require substantial RAM/GPU.
- The bot requires further improvement and scalability.
- Very long or ambiguous questions may still produce weak answers.
- Conversation history is ephemeral (resets on restart).