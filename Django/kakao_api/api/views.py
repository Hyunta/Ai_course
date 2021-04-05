from django.shortcuts import render
import json
import requests

def friends(request):
    return render(request, 'friends.html')

def mainpage(request):
    return render(request, 'main.html')


def login(request):
    authorization_code = request.GET.get('code')
    API_HOST = 'https://kauth.kakao.com'
    url = API_HOST + '/oauth/token'
    headers = {'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}

    data = {
        'grant_type': 'authorization_code',
        'client_id':  'd25760842535f66129f42677d12b2847',
        'redirect_uri': 'http://127.0.0.1:8000/api/login',
        'code': authorization_code
    }

    resp = requests.post(url, headers=headers, data=data)

    resp_json = json.loads(resp.text)
    print(resp_json)

    response = render(request, 'login.html')
    response.set_cookie('authorize-access-token', resp_json['access_token'], max_age=None)

    return response