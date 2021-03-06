import os

from src.word_predictor.iword_predictor_factory import ModelName, IWordPredictorFactory


class PredictWordProg:
    def __init__(self):
        self._text_history = ""

    def run(self, word_predictor, num_words=10):
        print("<Enter some text to get started...>")
        text = self.read_user_input()
        self._text_history = text
        word_predictor.feed(text)
        while True:
            self.display(word_predictor.top_n_next(num_words))
            text = self.read_user_input()
            self._text_history += text
            word_predictor.feed(text)

    def display(self, top_n_next):
        """
        Screen will look like so:
        --------------------------------------------
        Last n words written are shown here followed by______

        score   predicted_next_0
        score   predicted_next_1
        score   predicted_next_2
        score   predicted_next_3
        score   predicted_next_4

        > user_input
        --------------------------------------------

        :param top_n_next: list of 2-tuples (p, w) where w is a word and p is the likelihood of that word.
        """
        os.system("cls")
        print("{}____".format(self._text_history))
        print("")
        for p, w in top_n_next:
            print("{:3f}\t{}".format(p, w))
        print("")

    @staticmethod
    def read_user_input():
        return input("> ")


if __name__ == "__main__":
    PredictWordProg().run(IWordPredictorFactory().create_from_name(ModelName.GPT2_LARGE), 100)
