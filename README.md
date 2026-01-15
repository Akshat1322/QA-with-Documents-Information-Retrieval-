cat <<EOF > README.md
# 📄 QAWithPDF - Chat with Documents using Gemini 3.0

**QAWithPDF** is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content in natural language. 

Built with **Streamlit**, **LlamaIndex**, and **Google Gemini** (Flash models), this project demonstrates a modern, modular approach to building AI-powered QA systems with robust error handling and logging.

## 🚀 Features

* **📄 PDF Ingestion:** Upload and process PDF documents instantly.
* **🧠 Advanced RAG Pipeline:** Uses LlamaIndex for efficient vector storage and retrieval.
* **⚡ Powered by Gemini:** Utilizes Google's **Gemini 2.0 Flash / 3.0 Flash Preview** for high-speed, accurate responses.
* **🔍 Custom Embeddings:** Uses \`text-embedding-004\` for high-quality vector representations.
* **🛠️ Production-Grade Engineering:** Includes custom logging, exception handling, and modular code architecture.
* **💻 Interactive UI:** User-friendly interface built with Streamlit.

---

## 📂 Project Structure

\`\`\`text
QAGEMINI/
├── QAWithPDF/               # Core Application Logic
│   ├── __init__.py          # Package initialization
│   ├── data_ingestion.py    # Handles loading and processing PDFs
│   ├── embedding.py         # Manages VectorStore and Embeddings
│   └── model_api.py         # Configures the Gemini LLM
├── Experiments/             # Testing Playground
│   └── experiment.ipynb     # Jupyter notebook for testing logic
├── logs/                    # Runtime logs (Auto-generated)
├── Data/                    # Temporary storage for uploaded files
├── storage/                 # Local Vector Database persistence
├── StreamlitApp.py          # Main Frontend Application
├── logger.py                # Custom Logging Configuration
├── exception.py             # Custom Exception Handling
├── setup.py                 # Package Setup
├── requirements.txt         # Project Dependencies
├── .env                     # API Keys (Not tracked in Git)
└── .gitignore               # Git Ignore Rules
\`\`\`

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
\`\`\`bash
git clone <repository-url>
cd QAGEMINI
\`\`\`

### 2. Create a Virtual Environment (Recommended)
\`\`\`bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
\`\`\`

### 3. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Configure API Keys
Create a \`.env\` file in the root directory and add your Google API Key:
\`\`\`env
GOOGLE_API_KEY=your_google_api_key_here
\`\`\`
> **Note:** Get your free API key from [Google AI Studio](https://aistudio.google.com/).

---

## ▶️ How to Run

To start the application, run the Streamlit frontend:

\`\`\`bash
streamlit run StreamlitApp.py
\`\`\`

The application will open in your browser at \`http://localhost:8501\`.

1.  **Upload** a PDF document using the sidebar or upload area.
2.  Click **"Submit & Process"** to ingest the file.
3.  Type your question in the text box (e.g., *"Summarize this document"* or *"What is the main conclusion?"*).
4.  Wait for Gemini to generate the answer!

---

## 🔧 Technical Details

* **LLM:** Google Gemini 2.0 Flash / 3.0 Flash Preview (via \`llama-index-llms-gemini\`)
* **Embeddings:** Google \`text-embedding-004\`
* **Orchestration:** LlamaIndex (v0.10+)
* **Frontend:** Streamlit
* **Vector Store:** Local File Storage (Persisted via LlamaIndex \`StorageContext\`)

---

## 🔮 Future Improvements
* Add **Chat Memory** to support follow-up questions.
* Integrate **LlamaParse** for better handling of tables and complex formatting.
* Deploy to **Streamlit Cloud** or **Hugging Face Spaces**.
* Migrate vector storage to a cloud vector database (e.g., Pinecone or Weaviate).

---

## 📝 License
This project is open-source and available under the MIT License.
EOF