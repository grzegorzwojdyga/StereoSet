import json

from Translation import DeepL

file_name = "data/dev.json"


deepl = DeepL()
sentence = "I have no idea which room should I clean."
translation = deepl.translate(sentence)
print(translation)

with open(file_name, 'r') as f:
    data = json.load(f)
    print(data.keys())


