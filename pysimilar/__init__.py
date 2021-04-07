import os
import sys
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


class Pysimilar(object):
    """Very light library for computing similarity between two string or text documents

    Args:
        object ([type]): [description]
    """

    def compare(self, string_a: str, string_b: str) -> float:
        """Returns the similarity score between string a and string b 

        Args:
            string_a ([str]): [description]
            string_b ([str]): [description]

        Returns:
            float: [Similarity score between string a and string b ]
        """

        corpus = [string_a, string_b]
        vector_a, vector_b = self.string_to_vector(corpus)
        return self.compute_similarity(vector_a, vector_b)

    def compute_similarity(self, vector_a: list, vector_b: list) -> float:
        """Compute the similarity between vector a and vector b

        Args:
            vector_a (list): [description]
            vector_b (list): [description]

        Returns:
            float: [ int: [similarity score between vector a, string b]]
        """

        return cosine_similarity([vector_a, vector_b])[0][1]

    def string_to_vector(self, string: str) -> list:
        """Convert a list string to vectors using TfidfVectorizer

        Args:
            List (str): [description]

        Returns:
            list: [arrays of vectorized text]
        """
        return TfidfVectorizer().fit_transform(string).toarray()


sys.modules[__name__] = Pysimilar()
