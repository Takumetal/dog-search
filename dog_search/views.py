from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import random


URL = 'https://api.cognitive.microsoft.com/bing/v7.0/images/search'
API_KEY = ''


class IndexView(TemplateView):
    template_name = 'dog_search/index.html'

    def get(self, *args, **kwargs):
        context = {}
        return self.render_to_response(context) 

    def post(self, *args, **kwargs):
        headers = {'Ocp-Apim-Subscription-Key': API_KEY}
        params = {
            'q': self.request.POST['dog'],
            'count': '10',
            'offset': random.randint(0, 1000),
            'mkt': 'ja-JP',
        }
        response = requests.get(URL, headers=headers, params=params)
        data = response.json()
        values = data['value']
        results = []
        child_results = []

        for value in values:
            child_results.append(value['contentUrl'])
            if len(child_results) == 4:
                results.append(child_results)
                child_results = []
        else:
            results.append(child_results)

        context = {'results': results}
        return self.render_to_response(context)
