from django.shortcuts import render
from django.http import HttpResponse
import torch
from transformers import BertJapaneseTokenizer
from transformers import BertForSequenceClassification,BertConfig
import torch.nn.functional as F
from .models import GitProject
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World")

def search_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        MODEL_NAME = 'cl-tohoku/bert-base-japanese-whole-word-masking'
        tokenizer = BertJapaneseTokenizer.from_pretrained(MODEL_NAME)
        bert_sc = BertForSequenceClassification.from_pretrained(
            './model_transformers/'
        )
        bert_sc.eval()
        # 分析したいテキスト
        

        # テキストをトークナイズしてテンソルに変換
        inputs = tokenizer(query, return_tensors="pt")
        # 推論を実行（勾配計算は不要）
        with torch.no_grad():
            outputs = bert_sc(**inputs)

        logits = outputs.logits
        # ロジットから予測されたクラスIDを取得
        predicted_class_id = outputs.logits.argmax(-1).item()
        probabilities = F.softmax(logits, dim=-1)
        probabilities_list = probabilities[0].tolist()  # リストに変換してJavaScriptに渡す
        predicted_probability = probabilities[0, predicted_class_id].item()
        category_list = [
        'API',
        'ECサイト',
        '動画投稿アプリ',
        'snsアプリ',
        'WebRTC'
        ]
        predicted_category = category_list[predicted_class_id]
        print(f"Predicted category: {predicted_category}")
        matching_project = GitProject.objects.filter(title=predicted_category)
        context = {
            'probabilities_list': probabilities_list,
            'predicted_category': predicted_category,
            'predicted_probability': predicted_probability * 100,  # パーセンテージ表記
            'query': query,
            'matching_project': matching_project
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')
    
        
