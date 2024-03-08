# LlamaIndex Hello World
This hello world tutorial will help you begin your journey in learning how to train your favorite LLM models on custom data using the LlamaIndex data framework.

### What you Will Learn
Imagine you have a handful of documents - like emails, articles, or code. LlamaIndex lets you ask questions about these documents, just like you would ask ChatGPT a question, but pretend ChatGPT has read through everything in your documents!

In this tutorial you'll learn how to,
- [ ] Setup your very first LlamaIndex environment
- [ ] Sharpen your Python skills in relation to utilizing LLMs
- [ ] Develop a basic understanding and architecture of training and querying your LLMs

### What is RAG?
There are a number of ways you can train your LLM on custom data. You can,
1. Fine-tune your own large language model (LLM): This is like teaching an intelligent program to understand your documents. It's powerful, but takes a lot of time, expertise, computing power, and money.
2. Bunch up all of your content and feed everything into your LLM upfront: You could just copy and paste all your documents into a question for a regular LLM to answer. This might work, but it's slow and expensive and there are not too many LLMs available that support such large contexts to begin with.
3. Retrieval-Augmented Generation (RAG): Instead of giving your LLM all the context upfront, you just tell it the important parts related to your question.

LlamaIndex takes this last approach - feeding the LLM only the relevant information for each question. This makes it faster and cheaper than the other methods.

## Setup
### Preliminary Environment Setup
We'll be using the Anaconda Python environment so be sure to follow the [installation instructions](https://docs.anaconda.com/free/anaconda/install/). Also, make sure you have *git* installed and accessible in your terminal.

Go ahead and clone this git repository,

`git clone https://github.com/roth-ben/llama-index-hello-world.git`

### Conda and Python Package Dependencies
Now you'll install the necessary dependencies in Python. Enter these into your terminal,

```
conda create -n llama-index python=3.10.13 anaconda
conda activate llama-index
conda install openai python-dotenv -y
pip install llama-index pinecone-client llama-index-vector-stores-pinecone "unstructured [local-inference]"
```

### API Keys
We'll be working with both the OpenAI LLMs and embeddings, and Pinecone's online vector database. You'll need to create new API keys for both. On Pinecone, you'll also need to create a new index. Now open the *.env* file in your newly created local folder and enter in the API keys, index names, and Pinecone regional environment you've created your index in.

```
OPENAI_API_KEY=
PINECONE_ENVIRONMENT=
PINECONE_INDEX=
PINECONE_API_KEY=
```

## Up and Running
### Gather your Training Data
For this tutorial we're simply going to download the LlamaIndex website HTML files. We're going to train our LLM on the data available on their website so we can ask questions about the LlamaIndex framework. To do this you can simply run,

```
python download_docs.py
```

### Transform your Documents into Embeddings
Now we need to transform the text in these documents into embedding vectors so we can later be able to narrow down our RAG context that is input into our LLM model. Execute the ingestion file,

```
python ingestion.py
```

The ingestion process carries out the following tasks,
- Downloads all the relevant HTML files into the *./llamaindex-docs* directory.
- Using OpenAI's latest embedding model *text-embedding-3-small*, it transforms the LlamaIndex documents into vector embeddings.
- Uploads these embeddings into the Pinecode vector database.

### Query your LLM
Once the above ingestion process is complete, we can start to query our LLM using these documents as the basis of our context. Here we ask our LLM a simple and preliminary question, which you can update in code.

> What is a LlamaIndex query engine?

Execute the main Python file to run the query,

```
python main.py
```

This may take a few seconds but your results should come back with the added tracer information.

```
**********
Trace: index_construction
**********
**********
Trace: query
    |_agent_step ->  5.259178 seconds
      |_llm ->  0.852321 seconds
      |_function_call ->  3.251905 seconds
        |_query ->  3.251773 seconds
          |_retrieve ->  1.616533 seconds
            |_embedding ->  0.216524 seconds
          |_synthesize ->  1.63507 seconds
            |_templating ->  1.9e-05 seconds
            |_llm ->  1.62794 seconds
      |_llm ->  1.153354 seconds
**********
A LlamaIndex query engine is a component that utilizes Large Language Models (LLMs) to fetch data from an index and make decisions on where to find the information being sought. It can also transform retrieved data into a coherent answer or another programmatic output format.
```

## Next Steps
I hope you've been successful in setting up your very first LlamaIndex environment and have been able to ingest the documents and queried your LLM. In the upcoming tutorials I will show you how to build a quick user interface so you can interact with your LLM dynamically without the need to hardcode your questions.

Thanks!