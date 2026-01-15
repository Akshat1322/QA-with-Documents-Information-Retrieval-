import streamlit as st
import os

# Option 2 Imports (If you used __init__.py)
# from QAWithPDF import load_data, download_gemini_embedding, load_model

# Option 1 Imports (Direct imports)
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model


def main():
    st.set_page_config(page_title="QA with Documents")

    st.header("QA with Documents (Information Retrieval)")

    # Allow uploading PDF files
    doc = st.file_uploader("Upload your document", type=["pdf"])

    user_question = st.text_input("Ask your question")

    if st.button("Submit & Process"):
        if doc is not None:
            with st.spinner("Processing..."):
                try:
                    # --- CRITICAL FIX START ---
                    # 1. Create a temporary 'Data' directory
                    data_dir = "Data"
                    os.makedirs(data_dir, exist_ok=True)

                    # 2. Save the uploaded file to that directory
                    file_path = os.path.join(data_dir, doc.name)
                    with open(file_path, "wb") as f:
                        f.write(doc.getbuffer())

                    # 3. Now pass the DIRECTORY path to your function
                    # (SimpleDirectoryReader reads all files in this folder)
                    document = load_data(data_dir)
                    # --- CRITICAL FIX END ---

                    # 4. Load Model and Create Embeddings
                    model = load_model()
                    query_engine = download_gemini_embedding(model, document)

                    # 5. Query
                    response = query_engine.query(user_question)

                    st.success("Analysis Complete!")
                    st.write(response.response)

                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please upload a document first.")


if __name__ == "__main__":
    main()