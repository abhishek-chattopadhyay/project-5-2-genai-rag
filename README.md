![logo](./image/logo.png)

# RoboRecht: Your Assistant Lawyer Powered With AI
I belong to an international community in Germany and most of the times it is hard for me to understand the laws in Germany as they are in German and highly convoluted. This led me to develop **RoboRecht**, an AI-powered bot which can reply in easy words about the laws in Germany. It is based on RAG system and uses OpenAI GPT-4o model at its backend.

# Dataset collection
In the `data` folder, you will find the PDFs which contain the laws in Germany in English. These are open source documents and you can use it too. 
- Source: [German Bundestag](https://www.bundestag.de/services/infomaterial)

# Information about the project
- Database: I have used `ChromaDB` to create the vector database in this project. You can change it according to your need.
- Text embedding model: `text-embedding-3-large` model is used for embedding the texts to vectors.
- LLM model: OpenAI GPT-4o model is used.
- OpenAI API: You need to have OpenAI API key to run the python code or the Jupyter notebook given in this work. Put your API key in the `.env` file and run the notebook or the python script.
- Python libraries: The necessary python modules are given in the `requiremnts.txt` file. Create a python environment and download the requiremnts using pip as `pip install requirements.txt`.
- Streamlit app: The script `app.py` is a Streamlit implementation of the `main.ipynb`. Install Streamlit along with the `requirements.txt` to run this app.


