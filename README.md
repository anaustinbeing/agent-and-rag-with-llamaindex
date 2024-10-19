## Agent and RAG with LlamaIndex

This project helps to answer questions about world happiness report (csv file) and saves the answer as note or sends them as email.
This leverages the concept of Agent to choose the right tool (take note, send email, happiness tool) and uses RAG with LlamaIndex to retrieve information from the world happiness report (csv file).

## How to start?

Clone the repo:

```
git clone https://github.com/anaustinbeing/agent-and-rag-with-llamaindex.git
```

Change Directory into the agent-and-rag-with-llamaindex:

```
cd agent-and-rag-with-llamaindex
```

Create a virtual env in Python:

```
python -m venv venv
```

Activate virtual env (in Windows):

```
venv\Scripts\activate
```

Activate virtual env (in non-Windows):

```
source venv\bin\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Add .env file to it with following content:

```
OPENAI_API_KEY='paste your openai api key here'
EMAIL_PASSWORD='paste sender email password (get it from the service provider)'
SENDER_EMAIL='paste sender email address here'
RECEIVER_EMAIL='paste receiver email address here'
```

Start the application:

```
python app.py
```
