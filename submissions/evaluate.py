import argparse, sys
import pandas as pd
from sklearn.metrics import f1_score

class Judger(object):
    def __init__(self, model_dir, test_dir, law_dir="law.txt", acc_dir="accu.txt"):
        self.model_dir = model_dir
        self.test_dir = test_dir
        self.law_dir = law_dir
        self.acc_dir = acc_dir

        self.load_mapper()
        df = self.load_test_data()


    def load_test_data(self):
        """Load test data from directory"""
        test_df = pd.read_csv(self.test_dir)
        test_df.relevant_articles = test_df.relevant_articles.apply(
        lambda line: line.split(","))

        test_df.accusation = test_df.accusation.apply(
        lambda line: line.split(","))
        return test_df


    def load_mapper(self):
        """Load law-index accu-index mapping"""
        self.law_mapper = {}
        with open(self.law_dir, "r") as f:
            laws = f.readlines()
            for i, law in enumerate(laws):
                self.item_mapper[law.strip()] = i + 1

        self.acc_mapper = {}
        with open(self.acc_mapper, "r") as f:
            accus = f.readlines()
            for i, accu in enumerate(accus):
                self.acc_mapper[accu.strip()] = i + 1


    def load_macro(self):
        """
        TODO : compute macro score
        """
        self.macro = 0.


    def load_micro(self):
        """
        TODO : compute micro score
        """
        self.micro = 0.


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description =
    """
    Evaluation script for the model
    """
    )

    parser.add_argument('--m', type=str, dest='model_dir',
    help='model directory')
    parser.add_argument('--t', type=str, dest='test_dir',
    help='test data directory')

    args = parser.parse_args()
    model_dir, test_dir = args.model_dir, args.test_dir
    sys.path.insert(0, model_dir)
