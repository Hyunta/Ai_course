01. 장고란?
  1) 웹 어플리케이션 프레임 워크
	웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적으로 
	데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함한다.

	기존의 웹 개발 : DB 생성 -> 테이블 생성 -> 웹 App 개발
	장고의 웹 개발 : 웹 App 개발 -> 적용


  2) 프레임워크란?
	애플리케이션 개발에 바탕이 되는 템플릿과 같은 역활을 하는 클래스들과 인터페이스의 집합

  3) 장고를 사용해 만들어진 사이트
	인스타, NASA, 빅버켓, Disqus, 모질라


02. MVT 패턴
	Model + View + Template
	웹 어플리케이션을 개발하는 데에 있어서 영역을 크게 위의 3가지로 나눈 것
	각각의 영역을 독립적으로 개발 가능

  1) Model
	사용자 또는 파이썬 프로그램과 DB가 주고받을 데이터

  2) View
	사용자의 요청에 대한 데이터들이 처리되는 부분
	실직적인 파이썬 동작 코드를 작성하는 부분

  3) Template
	웹페이지에서 사용자가 보게될 페이지의 모습을 구성하는 부분
	html, css, javascript 등


03. 첫 프로젝트 생성
  0) 개발 환경 설정
	파이참 설치

  1) 프로젝트 생성

  2) 장고 설치
	pip install django

  3) 프로젝트에 장고 적용
	django-admin startproject config .

  4) 장고 프로젝트 실행
	python manage.py runserver

01. 프로젝트 구성 파일
  1) manage.py: 장고의 다양한 명령어를 실행하기 위한 파일, 변경X
  2) config : 프로젝트의 설정 파일과 웹 서버 실행을 위한 파일이 들어 있다.
		이름이 꼭 config일 필요는 없다.
		단, 생성 후 변경하려면 매우 귀찮음.

    (1) __init__.py: 파이썬 2.X 버전과 호환을 위해 만들어진 파일, 여러 폴더에 생성됨, 지워도 무관
    (2) settings.py: 프로젝트에 다양한 설정에 관한 내용이 들어있는 파일
    (3) urls.py: 하나의 프로젝트에는 여러개의 urls 파일이 만들어지고 
		config 안의 urls 파일은 최초로 탐색되는 기준 urls 파일
		기준 urls 파일은 settings 파일에서 변경 가능
    (4) wsgi: 웹서버에 배포할 때 설정파일들을 연결해 주는 파이썬 파일 
		

02. App 폴더
	python manage.py startapp [앱 이름]

  1) __init__.py: 해당 폴더가 파이썬 모듈로 작동이 가능하도록 해주는 파일
  2) admin.py: 관리자가 접속하면 보이는 화면, 내장돼 있음
  3) app.py: 앱을 등록하는 기능을 함
  4) models.py : 장고 DB 관련된 파일 /  DB 사용계획, 정의, 연결 등의 다양한 설정들을 함
  5) tests.py : 테스트를 위한 파이썬 파일
  6) views.py : 실질적으로 파이썬 코드가 실행이 되는 부분, 클래스형, 함수형
  7) urls.py :  폴더 안에 없지만, 추가로 생성해서 사용해야 하는 파일
  8) migrations/ : 파이썬 모듈로 작동하는 폴더, 데이터 베이스 스키마 관련


03. App 생성
  1) 템플릿 구성
	html 파일 생성 및 수정

  2) 뷰 구성
    (1) views.py
	원하는 로직을 작성하고 템플릿에서 구성한 html파일을 반환해준다.

    (2) urls.py
	views.py에 지정한 함수를 실행해준다.


  3) 실습
    (1) App 생성
	python manage.py startapp [앱이름]

	config\settings.py 파일에서 INSTALLED_APPS에 본인 앱 추가
	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    'testapp',
	]

    (2) [앱이름]\views.py
	from django.shortcuts import render

	def test(request):
	    return render(request, 'test.html')

    (3) [앱이름]\templates 폴더 생성
	폴더에 html 파일 생성

    (4) [앱이름]\urls.py 파일 생성
	from django.urls import path
	from . import views
	
	urlpatterns = [
	    path('', views.test, name='test'),
	]

    (5) config\urls.py
	from django.contrib import admin
	from django.urls import path, include
	
	urlpatterns = [
	    path('test01/', include('test01.urls')),
	    path('admin/', admin.site.urls),
	]	






















