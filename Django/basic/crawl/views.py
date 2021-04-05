from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def webtoon(request):
    if request.method == "GET":
        return render(request, 'webtoon_g.html')

    if request.method == "POST":
        webtoon_url = request.POST["url"]

        driver = webdriver.Chrome('C:\DKU_DBMS\chromedriver.exe')
        driver.implicitly_wait(5)

        driver.get(webtoon_url)

        img_tags = driver.find_elements_by_xpath('//img[@alt="comic content"]')

        img_srcs = []
        for i in img_tags:
            img_srcs.append(i.get_attribute('src'))

        driver.quit()

    return render(request, 'webtoon_p.html',{'imgs':img_srcs})



def gourmet(request):
    if request.method == "GET":
        return render(request, 'gourmet_g.html')

    if request.method == "POST":
        place = request.POST['place']
        driver = webdriver.Chrome('C:\DKU_DBMS\chromedriver.exe')
        driver.implicitly_wait(5)

        driver.get('https://map.kakao.com/')

        input_search = driver.find_element_by_id('search.keyword.query')
        input_search.send_keys(place)
        input_search.send_keys(Keys.RETURN)

        place_list = []
        for name in driver.find_elements_by_class_name('link_name'):
            place_list.append(name.text)

        driver.quit()

        return render(request, 'gourmet_p.html', {'p_list':place_list})

