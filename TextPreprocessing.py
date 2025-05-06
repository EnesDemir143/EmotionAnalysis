import spacy

class TextPreprocessing:
    def __init__(self, data, is_punct=None, is_stop=None):
        self.data = data
        self.is_punct = is_punct
        self.is_stop = is_stop

    def __call__(self):
        b        
