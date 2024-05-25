from transformers import AutoTokenizer, AutoModel
import torch


class TextToVector:
    def __init__(self, model_name='bert-base-uncased'):
        """
        Initialize the TextToVector with a specific Hugging Face model.
        :param model_name: str, the model identifier from Hugging Face Model Hub.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def text_to_embedding(self, text):
        """
        Convert input text to embedding vector.
        :param text: str, input text to convert.
        :return: numpy array, the embedding vector.
        """
        inputs = self.tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        # We use the first token ([CLS] in case of BERT) to represent the whole text
        return outputs.last_hidden_state[:, 0, :].numpy()

'''Example use
def main():
    t2v = TextToVector()
    text = "def hello_world():\n    print('Hello, world!')"
    vector = t2v.text_to_embedding(text)
    print("Generated Vector:", vector)

if __name__ == '__main__':
    main()
'''