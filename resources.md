# Artificial intelligence (AI) and large language models (LLMs)

### Introduction to LLMs:
- Brief: https://www.youtube.com/watch?v=LPZh9BOjkQs
- More in depth: https://www.youtube.com/watch?v=KJtZARuO3JY
- Advanced: https://www.youtube.com/watch?v=9-Jl0dxWQs8&vl=en
- Courses
  - https://www.cs.cmu.edu/~mgormley/courses/10423/   

### Text classification / qualitative coding with LLMs
- Langextract https://github.com/google/langextract
- https://www.comet.com
- [CodeLLM](https://github.com/PerttuHamalainen/LLMCode)
- Paid services (ideal for many qualitative research applications and for ease-of-use, but may not be super flexible either in terms of what model you can use and how you can use them):
  - Atlas TI: https://atlasti.com/
  - Nvivo
  - Dedoose
  - OpenAI Deep Research?

### LLM APIs
- openrouter: access all models using the same code (similar to litellm but I like it more)
- lambda: rent time on GPU to download and run specific huggingface model pretty automatically (for models which might not be on openrouter)
- embeddings: huggingface or litellm

### Formatting outputs
- Grammar: https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md
  - only works with open source llama cpp (platform, not model) models
  - restricts tokens before they are generated instead of post-processing.

### AI Code Assistants
- https://www.builder.io/blog/cursor-vs-windsurf-vs-github-copilot

### AI Agents
- https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0###heading=h.pxcur8v2qagu
- https://openai.com/index/introducing-agentkit/
- https://github.com/aishwaryanr/awesome-generative-ai-guide/tree/main/free_courses/agentic_ai_crash_course?fbclid=IwdGRjcAMjpEFleHRuA2FlbQIxMQABHsEA62OUbsJolgJTWRpFaDSFGpStJXm_qjLqqKlDQkUgm_HXQ0h8V0dV3SWS_aem_-9JtyKNUmrCfRGb0MaoeFg
- course: https://llmagents-learning.org/sp25 
- https://generalagents.com/ace/
- Examples:
  - https://biomni.stanford.edu/
 
### AI for scientific disovery
- https://platform.futurehouse.org/

### AI and humor
- https://pln-fing-udelar.github.io/semeval-2026-humor-gen/ 

### AI sovereign, open source
- https://publicai.co/utility

### RAG
- https://microsoft.github.io/graphrag/ 

### AI for Scientific discovery
- https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents

### AI and values
- https://www.nejm.org/doi/abs/10.1056/NEJMra2214183

### AI privacy 
- Nasr et al (2023). Scalable Extraction of Training Data from (Production) Language Models. https://arxiv.org/abs/2201.10351
- Vamosi, S., Platzer, M., & Reutterer, T. (2022). AI-based re-identification of behavioral clickstream data. arXiv preprint arXiv:2201.10351.

### LLM and GPT style of writing
- Over-use of the em dash: https://www.nytimes.com/2025/09/18/magazine/chatgpt-dash-hyphen-writing-communication.html?smid=nytcore-ios-share&referringSource=articleShare

<!-- ----------------------------------------------------------------------------------------------------------------------------------------->

# AI, LLMs, and psychology/mental health

### LLMs and psychotherapy and mental health
- Low, D., Mair, P., Nock, M., & Ghosh, S. Text Psychometrics: Assessing Psychological Constructs in Text Using Natural Language Processing. 
- Google: Lawrence HR, Schneider RA, Rubin SB, Mataric ́ MJ, McDuff DJ, Jones Bell M. The Opportunities and Risks of Large Language Models in Mental Health JMIR Ment Health 2024;11:e59479 doi: 10.2196/59479
- First RCT for psychotherapy: Heinz, M. V., Mackin, D. M., Trudeau, B. M., Bhattacharya, S., Wang, Y., Banta, H. A., ... & Jacobson, N. C. (2025). Randomized trial of a generative ai chatbot for mental health treatment. NEJM AI, 2(4), AIoa2400802.
- Stade, E. C., Toward Responsible Development and Evaluation of LLMs in Psychotherapy
- Several LLMs have been shown to provide responses to clinical questions that are empathetic, accurate, and high quality:
  - Ayers JW, Poliak A, Dredze M, Leas EC, Zhu Z, Kelley JB, et al. Comparing physician and artificial intelligence chatbot responses to patient questions posted to a public social media forum. JAMA Intern Med. 2023;183: 589–596.
  - Giorgi S, Isman K, Liu T, Fried Z, Sedoc J, Curtis B. Evaluating generative AI responses to real-world drug-related questions. Psychiatry Res. 2024;339: 116058.
- when you control for who the person thinks is answering (AI vs human response), people prefer responses from human even if an AI model authored it (and they think it was a human): Rubin, M., Li, J. Z., Zimmerman, F., Ong, D. C., Goldenberg, A., & Perry, A. (2025). Comparing the value of perceived human versus AI-generated empathy. Nature Human Behaviour, 1-15.
- Analyzing EMA and deep phenotyping data: https://mentalhealth.bmj.com/content/28/1/e301817#T1

### AI and psychotherapy chatbots
- Kai AI: you chat with both a real human (on weekdays) and AI models via whatsapp or other messaging services. Audio or text. It automatically creates summaries, diaries, and dashboards. Automatically creating recommendations on what modules to work on (different subtypes of CBT, e.g., for insomnia; motivational interviewing; substance use). Use synthetic data to fine-tune SOTA models. 24/7 safety team. Constant prompt engineering to adapt to techniques and artificial therapist styles (young, shorter messages, etc).  

### LLMs and sychophancy
The problem of sychophancy (over-agreeing and not challenging enough): 
- Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., ... & Perez, E. (2023). Towards understanding sycophancy in language models. arXiv preprint arXiv:2310.13548.
- Malmqvist, L. (2025, June). Sycophancy in large language models: Causes and mitigations. In Intelligent Computing-Proceedings of the Computing Conference (pp. 61-74). Cham: Springer Nature Switzerland.

### LLMs and Psychology
- Mihalcea, R., Biester, L., Boyd, R. L., Jin, Z., Perez-Rosas, V., Wilson, S., & Pennebaker, J. W. (2024). How developments in natural language processing help us in understanding human behaviour. Nature Human Behaviour, 8(10), 1877-1889.
- Stade, E. C., Stirman, S. W., Ungar, L. H., Boland, C. L., Schwartz, H. A., Yaden, D. B., ... & Eichstaedt, J. C. (2024). Large language models could change the future of behavioral healthcare: a proposal for responsible development and evaluation. NPJ Mental Health Research, 3(1), 12.

### Mental health chatbots
Psychedelic counselor: https://chatgpt.com/g/g-680126b5bc288191a17c8b01d4cc4773-psychedelic-hotline?mc_cid=f4f0eb10e7&mc_eid=bf933975ba 

<!-- ----------------------------------------------------------------------------------------------------------------------------------------->

# Data Science

### Python

### Where to run code? IDE environments
- VScode (open source) or Cursor (similar to VSCode but with paid AI Agent support)
- Next-generation Python notebooks: https://marimo.io/ (instead of colab or jupyter lab)

### Get Data
- Open-source: Crawl website with LLM: https://github.com/unclecode/crawl4ai

### Machine learning courses
- https://substack.com/@hodgesj/note/c-143072067?r=25ypvo&utm_medium=ios&utm_source=notes-share-action 

<!-- ----------------------------------------------------------------------------------------------------------------------------------------->
# Design
- Typst: instead of latex, https://typst.app/
- Canva: for nondesigners
- Figma: for designers. modular, save section in one page and it populates everywhere. Prototype function for a demo since all pages are linked.
- Miro: mind map, etc. Example: https://miro.com/app/board/uXjVKqp1I6U=/ 


<!-- ----------------------------------------------------------------------------------------------------------------------------------------->

# Mental health 

### Reducing stigma
- World Health Organization. (2024). Mosaic toolkit to end stigma and discrimination in mental health. In Mosaic toolkit to end stigma and discrimination in mental health. https://www.who.int/europe/publications/i/item/9789289061384

### Suicide and Suicidal thoughts and behaviors

#### Suicide risk assessment
- Donnelly (2025). Exploring the Potential of Large Language Models for Automated Safety Plan Scoring in Outpatient Mental Health Settings. 

<!-- ----------------------------------------------------------------------------------------------------------------------------------------->


# Speech processing and acoustic analysis

### Speech to text / automated speech recognition
- fast and open source: https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2 

### Speech as a tool in clinical trials
- Screening tool: https://www.sciencedirect.com/science/article/abs/pii/S0165178124003901


<!-- ----------------------------------------------------------------------------------------------------------------------------------------->


<!-- ----------------------------------------------------------------------------------------------------------------------------------------->


  
 
