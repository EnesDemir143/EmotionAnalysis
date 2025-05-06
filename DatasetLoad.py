import pandas as pd


class Dataset:

    def __init__(self):
        self.splits = {'train': 'split/train-00000-of-00001.parquet', 'validation': 'split/validation-00000-of-00001.parquet', 'test': 'split/test-00000-of-00001.parquet'}
        self.dataset = pd.read_parquet("hf://datasets/dair-ai/emotion/" + self.splits["train"])

    def __call__(self):
        return self.dataset

if __name__ == '__main__':
    pass