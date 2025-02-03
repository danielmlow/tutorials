
If you want to use LLMs through API, you might want to deidentify your text data locally (on your computer) before submitting. They generally remove HIPA identifies (e.g., proper nouns). These are some options:

- https://github.com/jftuga/deidentify
- https://huggingface.co/StanfordAIMI/stanford-deidentifier-base
- https://pypi.org/project/anonymization/
- https://pypi.org/project/presidio-anonymizer/\
- https://lhncbc.nlm.nih.gov/scrubber/

There are probably newer ones on huggingface.They don't work at 100% accuracy (especially with foreign proper nouns), but will help. 