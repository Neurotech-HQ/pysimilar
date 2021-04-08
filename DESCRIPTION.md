
# pysimilar
A python library for computing the similarity between two string(text) based on cosine similarity made by [kalebu](https://github.com/Kalebu)

<a href="https://www.buymeacoffee.com/kalebuj" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>


How does it work ?
------------------

It uses Tfidf Vectorizer to transform the text into vectors and then obtained vectors are converted into arrays of numbers and then finally cosine similary computation is employed resulting to output indicating how similar they are.


Example of usage
----------------
Pysimilar allows you to either specify the string you want to compare directly or specify path to files containing string you want to compare.

Here an example on how to compare strings directly;

```python
>>> from pysimilar import compare
>>> compare('very light indeed', 'how fast is light')
0.17077611319011649
```

Here how to compare files with textual documents;

```python
>>> compare('README.md', 'LICENSE', isfile=True)
0.25545580376557886
```

All the Credits
---------------

All the Credits to [kalebu](https://github.com/Kalebu) and other future contributors 