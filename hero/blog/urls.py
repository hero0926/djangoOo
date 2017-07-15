from django.conf.urls import url
# . 현재 디렉토리에서 import
from . import views


# regex, function
# ^ 문자열의 시작 $ 문자열의 끝
# r(regex의 r이 아니라 escape 문자임) '^(문자 시작은 이거로 하고)$(끝나는건 이렇게 끝날거임)'(이 내용임)
# //d = r'/d'임
#
urlpatterns = [

    url(r'^$', views.post_list),
    # url(r'^sum/(?P<x>\d+)/$', views.mysum),
    # sum / 으로 시작해서 (?P 만약 \d에 맞으면 <x> x라는 인자로 return 할게.)
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
    #     sum/뭔가의 숫자/뭔가의 숫자/뭔가의 숫자/ 에 매칭

    # 10/20/30/40... 의 패턴?
    url(r'^sum/(?P<numbers>[0-9/]+)/$', views.mysum),

    # /hello/한글이름/나이/
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.myurl),


]