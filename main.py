from dotenv import load_dotenv
import os

load_dotenv()

from pinecone import Pinecone
from llama_index.core import VectorStoreIndex, ServiceContext
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core.callbacks import LlamaDebugHandler, CallbackManager

from llama_index.core.settings import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

if __name__ == "__main__":
    # initialize Pinecone
    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
    pinecone_index = pc.Index(name=os.environ["PINECONE_INDEX"])
    vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

    # debug LLM callback
    llama_debug = LlamaDebugHandler(print_trace_on_end=True)
    callback_manager = CallbackManager(handlers=[llama_debug])
    Settings.callback_manager = callback_manager

    # initialize LlamaIndex vector store
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

    # query LLM
    query = "What is a LlamaIndex query engine?"
    query_engine = index.as_chat_engine()
    response = query_engine.query(query)

    # print response
    print(response)