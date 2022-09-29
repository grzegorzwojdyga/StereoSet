import deepl
'''
Description: https://pypi.org/project/deepl/
'''

class DeepL(object):
    def __init__(self):
        self.auth_key = "b5e3d717-eb8b-f266-159e-51caeda566e3:fx"
        self.translator = deepl.Translator(self.auth_key)

    def translate(text, source="EN", target="PL"):
        result = self.translator.translate_text(text, source, target)
        return result.text


