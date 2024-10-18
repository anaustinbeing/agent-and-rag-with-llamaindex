import os
from dotenv import load_dotenv
load_dotenv()
from email_engine import email_engine
from note_engine import note_engine

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.readers.file import CSVReader

from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(StorageContext.from_defaults(persist_dir=index_name))
    return index


parser = CSVReader()
file_extractor = {'.csv': parser}
documents = SimpleDirectoryReader('./csvs/', file_extractor=file_extractor).load_data()

happiness_index = get_index(documents, "happiness")
happiness_engine = happiness_index.as_query_engine()

tools = [
    note_engine,
    email_engine,
    QueryEngineTool(
        query_engine=happiness_engine,
        metadata=ToolMetadata(
            name="Happiness",
            description="This tool gives details about happiness scores and rankings.",
        ),
    )
]

llm = OpenAI(model="gpt-4o-mini")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context='This agent helps in note taking, email sending and get details about happiness scores and rankings.')

while True:
    prompt = input('Enter question (q to quit): ')
    if prompt.lower() == 'q':
        break
    result = agent.query(prompt)
    print(result)