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
- **Conversational memory**: carries context turn-to-turn per user  
- **Free & local**: no paid APIs; run everything on your own hardware  

## 📦 Installation

1. **Clone the repo** 
2. **Create & activate a venv**
3. **Install dependencies**
4. **Set up your environment**

## ⚙️ Usage

1. **Embed your docs (only first run or when data changes):**
- Run embed.py
2. **Start the bot:**
- Run bot.py

## 🏗 Architecture

1. **Data ingestion**
- embed.py reads .txt data files, chunks them, embeds with Sentence-Transformers, and stores vectors in FAISS.
2. **Retrieval-augmented generation**
- qa_pipeline.py loads FAISS + a local LLM (e.g. Flan-T5-large or Llama-2).
- Builds a ConversationalRetrievalChain with per-chat memory.
3. **Telegram integration**
- bot.py listens for messages, checks “in scope” with a quick FAISS similarity search, invokes the chain, logs the Q&A, and replies.

## ⚠️ Limitations
- Locally hosted LLMs may require substantial RAM/GPU.
- The bot requires further improvement and scalability.
- Very long or ambiguous questions may still produce weak answers.
- Conversation history is ephemeral (resets on restart).