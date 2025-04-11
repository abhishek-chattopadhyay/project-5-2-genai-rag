![logo](./image/logo.png)

# RoboRecht: Your AI-Powered Legal Assistant

Understanding German laws can be challenging—especially for international residents facing language barriers and complex legal language. To address this, I developed **RoboRecht**, an AI-powered assistant that explains German laws in simple, easy-to-understand language. Built using a Retrieval-Augmented Generation (RAG) architecture and powered by OpenAI's GPT-4o model, RoboRecht makes legal information more accessible and user-friendly.

## 📚 Dataset Collection

The `data` folder contains open-source English translations of German laws in PDF format.

- **Source:** [German Bundestag](https://www.bundestag.de/services/infomaterial)

## 🔧 Project Architecture

- **Vector Database:** `ChromaDB` is used for storing and querying document embeddings. You can replace it with your preferred vector database.
- **Embedding Model:** `text-embedding-3-large` from OpenAI for transforming text into vector representations.
- **LLM Model:** OpenAI `GPT-4o` model powers the legal Q&A generation.
- **API Key:** Ensure you have a valid OpenAI API key. Store it securely in a `.env` file to run the notebook or scripts.
- **Python Libraries:** All required libraries are listed in `requirements.txt`. Install them with:
  ```bash
  pip install -r requirements.txt
  ```
## 🚀 Streamlit App
A user-friendly web interface is implemented using Streamlit.
- Main Script: `app.py` serves as the front-end interface for the assistant.
- Setup: Install Streamlit along with the required dependencies:
```bash
pip install -r requirements.txt
streamlit run app.py
```
## 📂 Project Structure
```bash
RoboRecht/
│
├── app.py                # Streamlit application
├── main.ipynb            # Jupyter notebook with full pipeline
├── .env                  # File to store your OpenAI API key
├── data/                 # Contains PDF files of German laws
├── image/                # Contains project logo
├── requirements.txt      # List of required Python libraries
```
## 📬 Contact
For questions, feedback, or collaboration, feel free to connect via [LinkedIn](linkedin.com/in/abhishekchemistry/).  
**Disclaimer**: RoboRecht is intended for informational purposes only and does not constitute legal advice.

