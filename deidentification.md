
If you want to use LLMs through API, you might want to deidentify your text data locally (on your computer) before submitting. They generally remove HIPA identifies (e.g., proper nouns). 

The best option would probably be running an opensource LLM (Lama, deepseek) locally instructing to remove that from the text, but that would likely require a big GPU. 


These are some low-processing options:

- https://pypi.org/project/presidio-anonymizer/
- https://github.com/jftuga/deidentify
- https://huggingface.co/StanfordAIMI/stanford-deidentifier-base
- https://pypi.org/project/anonymization/
- https://lhncbc.nlm.nih.gov/scrubber/

There are probably newer ones on huggingface.They don't work at 100% accuracy (especially with foreign proper nouns), but will help. 