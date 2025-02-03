
If you want to use LLMs through API, you might want to deidentify your text data locally (on your computer) before submitting. These are some options:
https://github.com/jftuga/deidentify
https://huggingface.co/StanfordAIMI/stanford-deidentifier-base
https://pypi.org/project/anonymization/
https://pypi.org/project/presidio-anonymizer/
https://lhncbc.nlm.nih.gov/scrubber/

They don't work at 100% accuracy, but will help. 