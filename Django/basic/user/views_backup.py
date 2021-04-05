from django.shortcuts import render

def login(request):
    return render(request, 'login2.html')

def do_login(request):
    if request.method == "GET":
        id = request.GET['id']
        print('id = ' +id)

    fruits = ['tomato', 'mango', 'watermelon']
    return render(request, 'result.html', {'fruits': fruits})

def test(request):
    if request.method == "GET":
        return render(request, 'test1.html')

    if request.method == "POST":
        return render(request, 'test2.html')