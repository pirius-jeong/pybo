from django.http import HttpResponse


def index(request):
    return HttpResponse("공부방에 오신것을 환영합니다.")
