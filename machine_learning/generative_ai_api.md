# Test out OpenSource models on quick servers
- Go to Arena (side-by-side) or Direct Chat: https://chat.lmsys.org/
- This can help you decide if you want to try to get these running locally 

### Promptify

General purpose: works for many different NLP tasks and has defaulta prompts to start playing with. Can access Main Gen AI libraries OpenAI, ModelHub() for huggingface and others it says.

- https://github.com/promptslab/Promptify
- examples: https://github.com/promptslab/Promptify/blob/main/notebooks/examples.ipynb
- classification: https://github.com/promptslab/Promptify/blob/main/notebooks/classification.ipynb
- using huggingface models: https://github.com/promptslab/Promptify/blob/main/notebooks/huggingface.ipynb
- default prompts: https://github.com/promptslab/Promptify/tree/main/promptify/prompts
- unstructured to structured/tabular data: https://github.com/promptslab/Promptify/blob/main/notebooks/tabular.ipynb
- topic modeling: https://github.com/promptslab/Promptify/blob/27a53fa8e8f2a4d90f887d06ece65a44466f873a/promptify/prompts/text2text/topic_modelling/topic_modeling_draft.jinja#L5

### Skorch: text classification with sklearn-style syntax 
- https://skorch.readthedocs.io/en/latest/user/LLM.html 
- Advantages: you can use sklearn functions like do GridSearchCV, predict_proba() etc. 
- Disadvatanges: Only good for classification, not other NLP tasks


### LangChain
- Better for production/deployment
- https://www.langchain.com/ 
- https://python.langchain.com/docs/get_started/quickstart

### OpenLLM: better for open-source querying
- https://github.com/bentoml/OpenLLM
- https://colab.research.google.com/github/bentoml/OpenLLM/blob/main/examples/openllm-llama2-demo/openllm_llama2_demo.ipynb###scrollTo=Wyiz3fLoBeJ2
- Disadvantages: Doesn't have the pre-configured prompts that promptify and skorch have


### OpenAI API
Most of the above packages can access OpenAI and other models, so check them out first
- Examples: https://platform.openai.com/examples
- Code: https://github.com/openai/openai-cookbook/tree/main/examples
- Prices: https://openai.com/pricing###language-models

