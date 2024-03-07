# llama-index-hello-world
This hello world tutorial will help you begin your journey in learning how to train your LLM models on customer data using the LlamaIndex data framework.

## What you will learn
Here you'll learn how to,
- [ ] Setup your very first LlamaIndex environment on Docker
- [ ] Sharpen your Python skills in context to utilizing LLMs
- [ ] Develop a basic understanding and architecture of training your LLMs

Imagine you have a handful of documents - like emails, articles, or code. LlamaIndex lets you ask questions about these documents, just like you would ask ChatGPT a question, but pretend ChatGPT just read everything in your documents!

There are a number of ways do this, we will be focusing on the third method due 

1. Fine-tune your own large language model (LLM): This is like teaching an intelligent program to understand your documents. It's powerful, but takes a lot of time, expertise, computing power, and money.
2. Bunch up all of your content and feed everything into your LLM: You could just copy and paste all your documents into a question for a regular LLM to answer. This might work now, but it's slow and expensive and there are not too many LLMs available that support such large contexts to begin with.
3. Retrieval-Augmented Generation (RAG): Instead of giving your LLM all the context upfront, you just tell it the important parts related to your question.

LlamaIndex takes this last approach - feeding the LLM only the relevant information for each question. This makes it faster and cheaper than the other methods.