import streamlit as st
import os
import openai
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

def _get_document_prompt(docs):
    prompt = "\n"
    for doc in docs:
        prompt += "\nContent:\n"
        prompt += doc.page_content + "\n\n"
    return prompt

# Load API keys
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
embedding_function = OpenAIEmbeddings(model="text-embedding-3-large")

db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_function
)


# Streamlit UI Configuration
st.set_page_config(
    page_title="German Law AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# --- Header with Logo & Title ---
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image("../image/logo.png", use_container_width=True)

st.markdown(
    """
    <style>
        /* Style for text input (question box) */
        .stTextInput > div > div > input {
            border: 2px solid #1E90FF !important; /* Blue border */
            border-radius: 8px; /* Rounded corners */
            padding: 8px; /* Space inside */
            color: white !important; /* White text */
            background-color: black !important; /* Black background */
        }

        /* Centering the title and subtitle */
        .title-container {
            text-align: center;
            margin-bottom: 20px;
        }

        .title-container h2 {
            color: #1E90FF; /* Blue Title */
            font-size: 26px;
            margin-bottom: 5px;
        }

        .title-container p {
            color: white;
            font-size: 18px;
            margin-top: 0;
        }
    </style>
    
    <div class='title-container'>
        <h2>The Laws for the Federal Republic of Germany</h2>
        <p>Your AI-powered assistant for the laws in Germany</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""<br><br>""", unsafe_allow_html=True)  # Spacer

# --- Initialize Chat History ---
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# --- Display Chat History ---
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- User Input ---
user_question = st.chat_input("Ask me anything about German laws...")

if user_question:
    st.session_state["messages"].append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    # --- Processing Animation ---
    with st.spinner("Grab your beer and let me think... 🤔"):

        retrieved_docs = db.similarity_search(user_question, k=10)

        context_text = _get_document_prompt(retrieved_docs)

        prompt = f"""
        ## SYSTEM ROLE
        You are a knowledgeable and factual chatbot designed to assist with questions about **The Laws of the Federal Republic of Germany**, 
        specifically focusing on **Human Rights**. 
        Your answers must be based exclusively on provided content from the article provided.

        ## USER QUESTION
        The user has asked: 
        "{user_question}"

        ## CONTEXT  
        '''
        {context_text}
        '''
        
        ## RESPONSE FORMAT
        **Answer:** [Concise response, don't hallucinate.]

        📌 **Key Insights:**
        - Bullet point 1
        - Bullet point 2

        **Source**:  
        • [Article Title], Page(s): [...]
        """
        
        print("Prompt constructed.")

        # Set up GPT client and parameters
        client = openai.OpenAI()
        model_params = {
        'model': 'gpt-4o',
        'temperature': 0.7,  # Increase creativity
        'max_tokens': 4000,  # Allow for longer responses
        'top_p': 0.9,        # Use nucleus sampling
        'frequency_penalty': 0.5,  # Reduce repetition
        'presence_penalty': 0.6    # Encourage new topics
        }

        messages = [{'role': 'user', 'content': prompt}]
        completion = client.chat.completions.create(messages=messages, **model_params, timeout=120)
        answer = completion.choices[0].message.content

    # --- Display AI Response ---
    st.session_state["messages"].append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)