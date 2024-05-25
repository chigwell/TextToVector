[![PyPI version](https://badge.fury.io/py/TextToVector.svg)](https://badge.fury.io/py/TextToVector)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/TextToVector)](https://pepy.tech/project/TextToVector)

# TextToVector

`TextToVector` is a Python package designed to convert text into embedding vectors using Hugging Face models. This tool simplifies the process of generating embeddings for any given text, facilitating easy integration into NLP pipelines or machine learning models.

## Installation

To install `TextToVector`, you can use pip:

```bash
pip install TextToVector
```

## Usage

`TextToVector` is straightforward to use in your Python projects. Here's a quick example:

```python
from text_to_vector import TextToVector

t2v = TextToVector(model_name='bert-base-uncased')
text = "def hello_world():\n    print('Hello, world!')"
vector = t2v.text_to_embedding(text)
print("Generated Vector:", vector)
```

This package is especially useful for applications requiring text representations, such as semantic analysis, information retrieval, or machine learning models where text data needs to be converted into numerical form.

## Features

- Easy generation of embedding vectors from text.
- Utilizes state-of-the-art models from Hugging Face.
- Supports customization of model choices.
- Lightweight and easy to integrate.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/TextToVector/issues).

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
