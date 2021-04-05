from django.shortcuts import render
from django.conf import settings
from urllib import request as requ
import requests, json

users = {}

def settoken(request):
    myid = request.POST.get('myid')
    mytoken = request.POST.get('mytoken')

    users[myid] = mytoken

    print('myid : ' + myid)
    print('mytoken : ' + mytoken)
    return render(request, 'friends.html')

def friends(request):
    authorization_code = request.GET.get('code')

    kakao_restapi_key = getattr(settings, 'KAKAO_RESTAPI_KEY')

    API_HOST = 'https://kauth.kakao.com'
    url = API_HOST + '/oauth/token'

    headers = {'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}

    data = {
        'grant_type': 'authorization_code',
        'client_id': kakao_restapi_key,
        'redirect_uri': 'http://127.0.0.1:8000/friends',
        'code': authorization_code
    }

    resp = requests.post(url, headers=headers, data=data)

    resp_json = json.loads(resp.text)

    access_token = resp_json['access_token']

    kakao_js_key = getattr(settings, 'KAKAO_JS_KEY')
    firebase_config = getattr(settings, 'FIREBASE_CONFIG')
    firebase_vapidKey = getattr(settings, 'FIREBASE_VAPIDKEY')

    response = render(request, 'friends.html', {'kakao_js_key' : kakao_js_key, 'firebase_config' : firebase_config, 'firebase_vapidKey' : firebase_vapidKey})
    response.set_cookie('authorize-access-token', access_token, max_age=None)

    return response


def main(request):
    kakao_js_key = getattr(settings, 'KAKAO_JS_KEY')
    kakao_redirectUri = getattr(settings, 'KAKAO_REDIRECTURI')
    return render(request, 'main.html', {'kakao_js_key' : kakao_js_key, 'kakao_redirectUri': kakao_redirectUri})


def chat(request):
    if request.method == "GET":
        to = request.GET.get('to')
        firebase_config = getattr(settings, 'FIREBASE_CONFIG')
        return render(request, 'chat.html', {'to' : to, 'firebase_config' : firebase_config})

    if request.method == "POST":
        message = request.POST.get('message')
        to = request.POST.get('to')
        to_token = users[to]
        print('-----------------------')
        print(to_token)
        print('-----------------------')

        url = 'https://fcm.googleapis.com/fcm/send'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'key=AAAAASzDvKs:APA91bHub_FN02PZqJdrVGIPok0HGRPkQs8P88m7HFrp1gyOQ8MCH0IzRjcMw6_WKTELuUMWuhMVlC3DbbZn5jbz8Fb6QwK5c9nW-I1Bh6NkI5aYoShPD9plLZ8HAGQLzC7UxuMRT0xs'}
        data = {
            "notification": {
                "body": message,
                "title": "알림",
                "click_action": "http://localhost:8080/"
            },
            "to": to_token
        }
        reqq = requ.Request(url, headers=headers, data=json.dumps(data).encode('utf-8'))
        res = requ.urlopen(reqq)
        print(str(res.status) + " | " + res.read().decode('utf-8'))

        return render(request, 'chat.html')

def fms(request):
    firebase_config = getattr(settings, 'FIREBASE_CONFIG')

    return render(request, 'firebase-messaging-sw.js', {'firebase_config' : firebase_config}, content_type="application/x-javascript")

