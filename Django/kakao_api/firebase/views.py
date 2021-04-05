from django.shortcuts import render
from urllib import request as requ
import json

def push (request):
    return render(request,'push.html')

def fms(request):
    return render(request, 'firebase-messaging-sw.js', content_type="application/x-javascript")

def send(request):
    if request.method == "GET":

        return render(request, 'send.html')

    if request.method == "POST":
        message = request.POST['message']
        user_token = request.POST['user_token']

        url = 'https://fcm.googleapis.com/fcm/send'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'key=AAAAASzDvKs:APA91bHub_FN02PZqJdrVGIPok0HGRPkQs8P88m7HFrp1gyOQ8MCH0IzRjcMw6_WKTELuUMWuhMVlC3DbbZn5jbz8Fb6QwK5c9nW-I1Bh6NkI5aYoShPD9plLZ8HAGQLzC7UxuMRT0xs'}
        data = {
            "notification": {
                "body": message,
                "title": "알림",
                "click_action": "http://localhost:8080/"
            },
            "to": user_token
        }
        reqq = requ.Request(url, headers=headers, data=json.dumps(data).encode('utf-8'))
        res = requ.urlopen(reqq)
        print(str(res.status) + " | " + res.read().decode('utf-8'))

        return render(request, 'send.html')