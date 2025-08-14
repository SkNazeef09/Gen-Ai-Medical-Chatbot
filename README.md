# Gen-Ai-Medical-Chatbot


An **AI-powered medical assistant** that combines **Generative AI** with **medical knowledge retrieval** to provide context-aware, human-like responses to health-related queries.  
This chatbot is built using **LangChain**, **OpenAI GPT models**, and **vector databases** like Pinecone or FAISS.  

> **Disclaimer:** This chatbot is for **educational purposes only** and should not replace professional medical advice.

---

##  Key Features
- ** Natural Language Understanding** – Engages in interactive, human-like medical conversations.
- ** Medical Knowledge Base** – Retrieves relevant answers from curated medical datasets and documents.
- ** Retrieval-Augmented Generation (RAG)** – Enhances GPT responses with context from a vector store.
- ** Memory Support** – Remembers previous messages for multi-turn conversations.
- ** Fast Search** – Uses vector embeddings for instant retrieval from large datasets.
- ** Flexible Deployment** – Can run locally, on cloud servers, or in a web app.
- ** Safety Filters** – Limits responses to appropriate and safe topics.

---

## 🛠️ Tech Stack

| Component           | Technology Used |
|---------------------|-----------------|
| **Language**        | Python 3.10+ |
| **LLM Provider**    | OpenAI GPT Models (gpt-3.5 / gpt-4) |
| **Framework**       | LangChain |
| **Vector DB**       | Pinecone / FAISS |
| **Web UI**          | Streamlit / Flask |
| **Data Processing** | Pandas, NumPy |
| **Environment**     | Conda / venv |
| **Version Control** | Git & GitHub |

---


---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Gen-AI-Medical-Chatbot.git
cd Gen-AI-Medical-Chatbot

---

### 2️⃣ Create & Activate Virtual Environment
conda create --name medchatbot python=3.10
conda activate medchatbot

---

### 3️⃣ Install Dependencies
pip install -r requirements.txt

---

### 4️⃣ Add API Keys

Create a .env file in the root directory and add:

OPENAI_API_KEY=your_openai_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENV=your_pinecone_environment

---

