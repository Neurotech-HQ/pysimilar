# [pysimilar](https://pypi.org/project/pysimilar)

[![Downloads](https://pepy.tech/badge/pysimilar)](https://pepy.tech/project/pysimilar)
[![Downloads](https://pepy.tech/badge/pysimilar/month)](https://pepy.tech/project/pysimilar)
[![Downloads](https://pepy.tech/badge/pysimilar/week)](https://pepy.tech/project/pysimilar)

A python library for computing the similarity between two string(text) based on cosine similarity made by [kalebu](https://github.com/Kalebu)

[![Become a patron](pictures/become_a_patron_button.png)](https://www.patreon.com/kalebujordan)

How does it work ?
------------------

It uses Tfidf Vectorizer to transform the text into vectors and then obtained vectors are converted into arrays of numbers and then finally cosine similary computation is employed resulting to output indicating how similar they are.

Installation
-------------
You can either install it directly from *Github* or use *pip* to install it, here is how you to install it directly from github;

```bash
$  git clone https://github.com/Kalebu/pysimilar
$  cd pysimilar
$ pysimilar -> python setup.py install

```

Installation with pip
----------------------

```python
$ pip install pysimilar
```

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

You can also compare documents with particular **extension** in a given directory, for instance let's say I want to compare all the documents with **.txt** in a **documents** directory here is what I will do;

Directory for documents used by the example below look like this

```bash
documents/
├── anomalie.zeta
├── hello.txt
├── hi.txt
└── welcome.txt
```

Here how to compare files of a particular extension

```python
>>> import pysimilar
>>> from pprint import pprint
>>> pysimilar.extensions = '.txt'
>>> comparison_result = pysimilar.compare_documents('documents')
>>> [['welcome.txt vs hi.txt', 0.6053485081062917],
    ['welcome.txt vs hello.txt', 0.0],
    ['hi.txt vs hello.txt', 0.0]]
```

You can also sort the comparison score based on their score by changing the **ascending** parameter, just as shown below;

```python
>>> comparison_result = pysimilar.compare_documents('documents', ascending=True)
>>> pprint(comparison_result)
[['welcome.txt vs hello.txt', 0.0],
 ['hi.txt vs hello.txt', 0.0],
 ['welcome.txt vs hi.txt', 0.6053485081062917]]
```

You can also set pysimilar to include files with multiple extensions

```python
>>> import pysimilar
>>> from pprint import pprint
>>> pysimilar.extensions = ['.txt', '.zeta']
>>> comparison_result = pysimilar.compare_documents('documents', ascending=True)
>>> pprint(comparison_result)
[['welcome.txt vs hello.txt', 0.0],
 ['hi.txt vs hello.txt', 0.0],
 ['anomalie.zeta vs hi.txt', 0.4968161174826459],
 ['welcome.txt vs hi.txt', 0.6292275146695526],
 ['welcome.txt vs anomalie.zeta', 0.7895651507603823]]

```

Contributions
-------------
If you have anything valuable to add to the *lib*, whether its a documentation, typo error, source code, please don't hesitate to contribute just fork it and submit your pull request and I will try to be as friendly as I can to assist you making the contributions.


Give it a star
--------------
Did you find this repo useful to you ? then give it a star so as more people can be aware of it and use it, Share that love *

All the Credits
---------------

All the Credits to [kalebu](https://github.com/Kalebu) and other future contributors 