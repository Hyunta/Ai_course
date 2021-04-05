from django.shortcuts import render

def login(request):
    if request.method == "GET":
        return render(request, 'login2.html')

    if request.method == "POST":
        did = request.POST['d_id']
        dpw = request.POST["d_pw"]
        print('id = ' +did)
        print('pw = ' + dpw)
        user_info = [did, dpw]
        return render(request, 'result.html',{'uinfos':user_info})

def do_login(request):
    if request.method == "POST":
        did = request.POST.get['d_id']
        dpw = request.POST.get["d_pw"]
        print('id = ' +did)
        print('pw = ' + dpw)
        user_info = [did, dpw]
        return render(request, 'result.html',{'uinfos':user_info})

def test(request):
    if request.method == "GET":
        return render(request, 'test1.html')

    if request.method == "POST":
        return render(request, 'test2.html')