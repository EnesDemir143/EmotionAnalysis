import numpy as np
import gensim

class FeatureEngineering:
    def __init__(self, data, epoch=20):
        self.data = data
        self.word2vec = gensim.models.Word2Vec(
            window=10,
            workers=10,
            min_count=2
        )
        self.epoch = epoch

    def _create_vocab(self):
        self.word2vec.build_vocab(self.data, progress_per=100)

    def _train_model_save(self):
        self._create_vocab()
        self.word2vec.train(self.data, epochs=self.epoch, total_examples=self.word2vec.corpus_count)
        self.word2vec.save("word2vec_emotion_data.model")

    def get_document_vectors(self, text):
        words_vectors = [self.word2vec.wv[word] for word in text if word in self.word2vec.wv]
        if not words_vectors:
            return np.zeros(self.word2vec.vector_size)
        doc_vector = np.mean(words_vectors, axis=0)
        return doc_vector

    def __call__(self):
        self._train_model_save()
        return self.word2vec

if __name__ == '__main__':
    pass