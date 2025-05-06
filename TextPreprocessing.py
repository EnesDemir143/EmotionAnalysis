import spacy

class TextPreprocessing:
    def __init__(self, data, is_punct=None, is_stop=None):
        self.data = data
        self.is_punct = is_punct
        self.is_stop = is_stop
        self.nlp = spacy.load('en_core_web_sm')

    def _preprocess_text(self):
        if not isinstance(self.data, str) or not self.data.strip():
            return ""  
        
        text = self.data.lower()
        doc = self.nlp(text)

        filtered_data = []
        for token in doc:
            if (self.is_punct and token.is_punct) or ( self.is_stop and token.is_stop):
                continue
        filtered_data.append(token.lemma_)

        return " ".join(filtered_data)

    def __call__(self):
        return self._preprocess_text()
    
if __name__ == '__main__':
    pass