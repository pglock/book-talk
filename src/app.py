from llama_pipeline import create_pipeline

from llama_index.query_engine.retriever_query_engine import RetrieverQueryEngine

import chainlit as cl


@cl.on_chat_start
async def factory():

    query_engine = create_pipeline("./books", "en")

    cl.user_session.set("query_engine", query_engine)


@cl.on_message
async def main(message: cl.Message):
    query_engine = cl.user_session.get("query_engine")  # type: RetrieverQueryEngine
    response = await cl.make_async(query_engine.query)(message.content)

    response_message = cl.Message(content="")

    for token in response.response_gen:
        await response_message.stream_token(token=token)

    if response.response_txt:
        response_message.content = response.response_txt

    await response_message.send()
