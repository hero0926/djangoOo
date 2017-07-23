
from django.conf.urls import url
# . 현재 디렉토리에서 import
from . import views
from . import views_cbv

# regex, function
# ^ 문자열의 시작 $ 문자열의 끝
# r(regex의 r이 아니라 escape 문자임) '^(문자 시작은 이거로 하고)$(끝나는건 이렇게 끝날거임)'(이 내용임)
# //d = r'/d'임
#
urlpatterns = [


    # url(r'^sum/(?P<x>\d+)/$', views.mysum),
    # sum / 으로 시작해서 (?P 만약 \d에 맞으면 <x> x라는 인자로 return 할게.)
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
    #     sum/뭔가의 숫자/뭔가의 숫자/뭔가의 숫자/ 에 매칭

    # 10/20/30/40... 의 패턴?
    url(r'^sum/(?P<numbers>[0-9/]+)/$', views.mysum),

    # /hello/한글이름/나이/
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.myurl),

    url(r'^$', views.post_list, name='post_list'),
    url(r'^new/$', views_cbv.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views_cbv.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),


]