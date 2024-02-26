# Book-Talk

Chat with your books using local LLMs.

## Get Started

- `poetry install`
- setup ollama
- `poetry shell`
- add epub files to the `books` directory
- `chainlit run src/app.py`

## Runs on

- [LLamaIndex](https://www.llamaindex.ai/) for the RAG pipeline
- [Ollama](https://ollama.com/) for running LLMs locally
- [chainlit](https://docs.chainlit.io/get-started/overview) for the Chat UI
- [sentence_transformers](https://www.sbert.net/) and [langchain](https://www.langchain.com/) for creating embeddings

## Todo

- [ ] persist index
- [ ] selectable profile for every epub
- [ ] support for german
