dog-search
====

犬の画像を取得して表示するアプリです。  
An app that retrieves and displays images of dogs.

## Description
Djangoで実装されています。  
It is implemented in Django.

## Requirement
Python3.6  
certifi==2018.11.29  
chardet==3.0.4  
Django==2.1.5  
idna==2.8  
pytz==2018.9  
requests==2.21.0  
urllib3==1.24.1

## Usage
1. Githubからリポジトリをクローン  
Clone repository from Github
```
$ git clone https://github.com/Takumetal/dog-search.git
```
2. プロジェクトディレクトリに入る  
Change the project directory
```
$ cd dog-search
```
3. pipを使用して、必要なライブラリをインストール  
Install required libraries using pip
```
$ pip install -r requirements.txt 
```
4. Azure Bing Image Search APIのAPIキーを取得して、以下に設定する  
Get the API key for the Azure Bing Image Search API and set it as follows.
```
dog_search/views.py
API_KEY = ''
```
5. Djangoの開発サーバーを起動  
Launch the development server for Django
```
$ python manage.py runserver
```
6. ブラウザで以下のURLにアクセス  
Access the following URL in a browser
```
http://127.0.0.1:8000
```

## Licence
MIT

## Author
[Takumetal](https://github.com/Takumetal)
