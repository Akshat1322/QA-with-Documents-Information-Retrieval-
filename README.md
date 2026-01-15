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




