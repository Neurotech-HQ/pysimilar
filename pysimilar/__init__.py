import os
import sys
from pathlib import Path
from typing import Union, List
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


class Pysimilar(object):
    """Very light library for computing similarity between two string or text documents

    Args:
        object ([type]): [description]
    """

    @staticmethod
    def load_file(path_to_file: Path):
        with open(path_to_file, 'r') as document:
            content = document.read()
        return content

    def compare(self, string_i: Union[str, Path], string_j: Union[str, Path], isfile=False) -> float:
        """Returns the similarity score between string i and string j 


        Args:
            string_i (Union[str, Path]): [description]
            string_j (Union[str, Path]): [description]

        Returns:
            float: [Similarity score between string i and string j ]
        """

        if not isinstance(string_i, (str, Path)) or not isinstance(string_j, (str, Path)):
            raise TypeError(
                'Both string i and string j must be of type either string or Path')

        if isfile:
            string_i, string_j = self.load_file(
                string_i), self.load_file(string_j)

        corpus = [string_i, string_j]
        vector_i, vector_j = self.string_to_vector(corpus)
        return self.compute_similarity(vector_i, vector_j)

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
