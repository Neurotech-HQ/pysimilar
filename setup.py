from distutils.core import setup

setup(
    name="pysimilar",
    version="0.2",
    description='A very light python libary for comparing similarity between text/strings',
    url='https://github.com/Kalebu/pysimilar',
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
        "python-tanzania"
    ],

    install_requires=[
        'scikit-learn',
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
