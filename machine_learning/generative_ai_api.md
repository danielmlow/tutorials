# Run text generative AI models

Options:

- NLP tasks: what tasks it tries to solve using generative AI. Many means it uses prompt templates to do classification, NER, topic modeling, summarization, etc.
- Provides prompts: some packages played around with prompts to give you a template for doing different tasks
- Local vs. API: Can you download the model so the data doesn't go to their servers
- Open source vs. proprietary: basically, free huggingface models vs. paid proprietary models accessed through an API


| **Package**    | **NLP tasks**  | **Provides prompts** | **Local vs. API** | **Open source vs. proprietary** | **Advantages**                           | **Disadvantages**                                          |
|----------------|----------------|----------------------|-------------------|---------------------------------|------------------------------------------|------------------------------------------------------------|
| **LiteLLM**     | Generative AI | No                   | API               | All                             | Easy access to all APIs                 | Not sure use of Huggingface API is free                     |
| **ollama**     | Generative AI | No                   | Local               | Open source (Huggingface)          | Local and Private                 | Only uses Huggingface models which may not work well                     |
| **GPT4all**     | Generative AI | No                   | Local               | Open source (Huggingface)          | Local and Private                 | Only uses Huggingface models which may not work well                     |
| **scikit-llm**  | Many           | Yes                  | Both | Both                            | Pre-configured prompts for different tasks, works on top of APIs and GPT4all                   | Not sure if it does simple requests and gridsearchCV |
| **Skorch**     | Classification | No                   | Local             | Open source (Huggingface)       | Sklearn syntax and hyperparameter tuning | Only does classification                                   |
| **LangChain**  | Generative AI  | No                   | API               | Both                            | Ideal for deploying                      |                                                            |
| **OpenLLM**    | Generative AI  | No                   | Both               | Open source (Huggingface)       | Ideal for deploying                                     | Tutorial didn't work for me                                |
| **Promptify**  | Many           | Yes                  | API (maybe local) | Both                            | Pre-configured prompts                   | Package is not well developed, tutorials will likely break |
| **OpenAI API** | Many | No                   | API               | Proprietary                     | Easy to use                              | Only OpenAI models                                         |


Leaderboards:
- Open LLMs: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
- Another huggingface one: https://llm-leaderboard.streamlit.app/
- Proprietary LLMs (not sure it is up to date): https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu

Data comparison:
- https://blog.allenai.org/dolma-3-trillion-tokens-open-llm-corpus-9a0ff4b8da64

Summary: 
- If you want to use GPT-4 or GPT-3.5 Turbo, you might just use OpenAI API. You'll have to pay a fraction of a cent per request. But I recommend using LiteLLM since it gives you access to all APIs with the same code (just adding the corresponding API key) so you can compare APIs (e.g., OpenAI vs Google vs Cohere, etc).
- For text classification on API models, I'd use skorch or scikit-llm.
- For text classification on huggingface models, I might use scikit-llm which might allow for gridsearchCV or skorch which has gridsearch cv. 
- For other tasks, I'd just use normal requests like NER I'd use litellm for API models and GPT4all for huggingface models or Hugginface's transformers package directly, and get inspirations for prompts from promptify and scikit-llm. 
- If you want to use free open-source models and compare models you might want to use
  - gpt4all for prompts
  - scikit-llm for text classification (zero-shot, multilabel, etc) and summarization, vectors, and finetuning
  - skorch just for text classification (but with gridsearchCV option)
  - promptify has some additional prompts, but the package is not well maintained (tutorials haven't been updated)
  - They say Llama-2 70b HF is currently (11/3/2023) producing results similar to GPT-4; however, you'll have to figure out how to run it on a few GPUs
  - Smaller and distilled models are available on huggingface [leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard), but performance will likely decrease for now.
- If you want to download the model locally, use GPT4all, skorch or openLLM which will download huggingface.
- If you want inspirations for prompts, go to https://github.com/promptslab/Promptify/tree/main/promptify/prompts/text2text

### LiteLLM
- Quick and easy way to access all APIs with the same code. Tools for deployment.

### Test out open-source models on quick servers
- Go to Arena (side-by-side) or Direct Chat: https://chat.lmsys.org/
- This can help you decide if you want to try to get these running locally 

### GPT4all
- https://github.com/nomic-ai/gpt4all/blob/main/gpt4all-bindings/python/README.md

### scikit-llm: text classification (and other NLP tasks) with sklearn-style syntax 
- https://github.com/iryna-kondr/scikit-llm
- Access to both APIs and GPT4all which uses local methods.
- Did not test wether everything works



### Skorch: text classification with sklearn-style syntax 
- Advantages: you can use sklearn functions like do GridSearchCV, predict_proba() etc. 
- Disadvatanges: Only good for classification, not other NLP tasks


### Promptify

The package is not well maintained. The beenfit is it provides many prompts to do many different NLP tasks. Can access Main Gen AI libraries OpenAI, `ModelHub()` for huggingface and others it says, however, getting ModelHub to run was tricky. You need to manually add model names to metadata.json within the task folder (e.g., `prompts/ner/metadata.json`)

- https://github.com/promptslab/Promptify
- examples: https://github.com/promptslab/Promptify/blob/main/notebooks/examples.ipynb
- classification: https://github.com/promptslab/Promptify/blob/main/notebooks/classification.ipynb
- using huggingface models: https://github.com/promptslab/Promptify/blob/main/notebooks/huggingface.ipynb
- default prompts: https://github.com/promptslab/Promptify/tree/main/promptify/prompts
- unstructured to structured/tabular data: https://github.com/promptslab/Promptify/blob/main/notebooks/tabular.ipynb
- topic modeling: https://github.com/promptslab/Promptify/blob/27a53fa8e8f2a4d90f887d06ece65a44466f873a/promptify/prompts/text2text/topic_modelling/topic_modeling_draft.jinja#L5

### LangChain
- Better for production/deployment
- https://www.langchain.com/ 

### OpenLLM: better for open-source querying
- https://github.com/bentoml/OpenLLM
- https://colab.research.google.com/github/bentoml/OpenLLM/blob/main/examples/openllm-llama2-demo/openllm_llama2_demo.ipynb###scrollTo=Wyiz3fLoBeJ2
- Disadvantages: Doesn't have the pre-configured prompts that promptify and skorch have

### OpenAI API
Most of the above packages can access OpenAI and other models, so check them out first
- Examples: https://platform.openai.com/examples
- Code: https://github.com/openai/openai-cookbook/tree/main/examples
- Prices: https://openai.com/pricing###language-models
- Limits to requests: https://github.com/openai/openai-cookbook/blob/main/examples/How_to_handle_rate_limits.ipynb 

### Replicate
- Can run many different Gen AI (audio, text, text to image, etc) models.
- https://replicate.com/meta/llama-2-70b-chat

### Prompt engineering
- https://replicate.com/blog/how-to-prompt-llama
- Skorch let's you treat different prompts as a hyperparameter values that you can finetune.
- https://app.promptify.com/

### Others

Each company has their own API: 
- Azure (Microsoft which has version of GPT-4)
- Cohere
- Google
- Anthropic
- etc


# Train / finetune LLMs
- https://github.com/hiyouga/LLaMA-Factory
- Lambda cloud
- litGPT
- https://novasky-ai.github.io/posts/sky-t1/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=450-reasoning-model-matches-o1&_bhlid=5ec2a25c55ec3a370bb1696fd306d9e0f5872481
