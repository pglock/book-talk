from llama_index import VectorStoreIndex,SimpleDirectoryReader,ServiceContext
from llama_index.llms import Ollama
from llama_index.prompts.prompts import SimpleInputPrompt

from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index import ServiceContext
from llama_index.embeddings import LangchainEmbedding


SYSTEM_PROMPT = {
    "en": """
    You are a Q&A assistant. Your goal is to answer questions as
    accurately as possible based on the instructions and context provided.
    """
}

def create_pipeline(document_dir, language):
    documents = SimpleDirectoryReader(document_dir).load_data()
    query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")
    system_prompt = SYSTEM_PROMPT[language]
    llm = Ollama(model="llama2", request_timeout=60.0, streaming=True)

    embed_model = LangchainEmbedding(
        HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    )

    service_context=ServiceContext.from_defaults(
        chunk_size=512,
        llm=llm,
        embed_model=embed_model,
        system_prompt=system_prompt,
        query_wrapper_prompt=query_wrapper_prompt
    )
    index = VectorStoreIndex.from_documents(documents,service_context=service_context)
    query_engine = index.as_query_engine(streaming=True)
    return query_engine
