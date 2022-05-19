from os import path
from setuptools import setup

# read the contents of your description file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "description.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pysimilar",
    version="0.5",
    description="A very light python libary for comparing similarity between text/strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kalebu/pysimilar",
    download_url="https://github.com/Kalebu/pysimilar/archive/0.2.tar.gz",
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=["pysimilar"],
    keywords=[
        "pysimilar",
        "python-plagiarism-library",
        "natural language processing",
        "NLP libary",
        "python-tanzania",
    ],
    install_requires=[
        "scikit-learn",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
