import spacy

class TextPreprocessing:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def preprocess_text(self, data):
        if not isinstance(data, str) or not data.strip():
            return ""  
        
        text = data.lower()
        doc = self.nlp(text)

        filtered_data = []
        for token in doc:
            if token.is_punct or token.is_stop:
                continue
            filtered_data.append(token.lemma_)

        return " ".join(filtered_data)

if __name__ == '__main__':
    pass