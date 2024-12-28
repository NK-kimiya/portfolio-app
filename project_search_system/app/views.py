from django.shortcuts import render
from .models import GitProject
from .bert.text_classifier import TextClassifier

classifier = TextClassifier()

def search_view(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        predicted_category, predicted_probability = classifier.predict_category(query)
        matching_project = GitProject.objects.filter(title=predicted_category)
     
        context = {
            'predicted_category': predicted_category,
            'predicted_probability': predicted_probability * 100,  
            'query': query,
            'matching_project': matching_project
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')
    
        
