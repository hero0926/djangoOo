from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# view 화면 연결
def post_list(request) :
    return render(request, "blog/post_list.html")


def mysum(request, numbers) :

    result = 0;
    for number in numbers.split("/") :

        if number : # 빈 문자열이 아니라 숫자가 있을 경우엔
            result += int(number)

        # result += int(number or 0) -> number가 거짓일시 뒤 값이 대신 사용


    # 또는 제너레이터 표현식으로 아래와 같이 표현 할 수도 있다

    # sum(int(number or 0) for number in numbers.split("/"))

    return HttpResponse(result)


def myurl(request, name, age) :

    return HttpResponse("안녕하세요, "+name+". "+age+"살이네요.")
