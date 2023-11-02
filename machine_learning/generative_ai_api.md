# Run text generative AI models

Options:

NLP tasks: what tasks it tries to solve using generative AI. Many means it uses prompt templates to do classification, NER, topic modeling, summarization, etc. 


| **Package**    | **NLP tasks**  | **Provides prompts** | **Local vs. API** | **Open source vs. proprietary** | **Advantages**                           | **Disadvantages**                                          |
|----------------|----------------|----------------------|-------------------|---------------------------------|------------------------------------------|------------------------------------------------------------|
| **Promptify**  | Many           | Yes                  | API (maybe local) | Both                            | Pre-configured prompts                   | Package is not well developed, tutorials will likely break |
| **Skorch**     | Classification | No                   | Local             | Open source (Huggingface)       | Sklearn syntax and hyperparameter tuning | Only does classification                                   |
| **LangChain**  | Generative AI  | No                   | API               | Both                            | Ideal for deploying                      |                                                            |
| **OpenLLM**    | Generative AI  | No                   | Both               | Open source (Huggingface)       |                                          | Tutorial didn't work for me                                |
| **OpenAI API** | Many NLP tasks | No                   | API               | Proprietary                     | Easy to use                              | Only OpenAI models                                         |


- If you want to use GPT-4 GPT-3.5 Turbo, you might just use OpenAI API. You'll have to pay a fraction of a cent per request.
- If you want to use free open-source models and compare models you might want to use
  - skorch for text classification or
  - promptify for other NLP tasks
  - Lama-2 70b is currently producing results similar to GPT-4; however, you'll have to figure out how to run it on a few GPUs
  - Smaller and distilled models are available, but performance will decrease.
- If you want to download the model locally, use skorch or openLLM which will download huggingface.
- If you want inspirations for prompts, go to https://github.com/promptslab/Promptify/tree/main/promptify/prompts/text2text

### Test out open source models on quick servers
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
-LangCh
- Advantages: you can use sklearn functions like do GridSearchCV, predict_proba() etc. 
- Disadvatanges: Only good for classification, not other NLP tasks

### LangChain
- Better for production/deployment
- https://www.langchain.com/ 
- Open

### OpenLLM: better for open-source querying
- https://github.com/bentoml/OpenLLM
- https://colab.research.google.com/github/bentoml/OpenLLM/blob/main/examples/openllm-llama2-demo/openllm_llama2_demo.ipynb###scrollTo=Wyiz3fLoBeJ2
- Disadvantages: Doesn't have the pre-configured prompts that promptify and skorch have

### OpenAI API
Most of the above packages can access OpenAI and other models, so check them out first
- Examples: https://platform.openai.com/examples
- Code: https://github.com/openai/openai-cookbook/tree/main/examples
- Prices: https://openai.com/pricing###language-models

### Others

Each company has their own API: 
- Azure (Microsoft which has version of GPT-4)
- Cohere
- Google
- Anthropic
- etc

