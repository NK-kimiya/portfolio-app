import torch
from transformers import BertJapaneseTokenizer,BertForSequenceClassification
import torch.nn.functional as F

class TextClassifier:
    def __init__(self):
        self.MODEL_NAME = 'cl-tohoku/bert-base-japanese-whole-word-masking'
        self.tokenizer = BertJapaneseTokenizer.from_pretrained(self.MODEL_NAME)
        self.model = BertForSequenceClassification.from_pretrained('./model_transformers/')
        self.model.eval()
        self.category_list = ['API', 'ECサイト', '動画投稿アプリ', 'snsアプリ', 'WebRTC']

    def predict_category(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_class_id = logits.argmax(-1).item()
        probabilities = F.softmax(logits, dim=-1)
        predicted_probability = probabilities[0, predicted_class_id].item()
        predicted_category = self.category_list[predicted_class_id]
        return predicted_category, predicted_probability