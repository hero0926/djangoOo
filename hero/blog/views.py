from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.db.models import Q
from django.shortcuts import redirect, render
from .forms import PostForm

# Create your views here.

# view 화면 연결
def post_list(request) :

    qs = Post.objects.all()
    
    # 쿼리에 해당하는 값 없을 시엔 ''공백 리턴

    query = request.GET.get('query', '')
    type = request.GET.get('type', '')

    #값이 있으면
    
    if query :
        #title__icontains -> 제목에 검색어가 있는 것만 필터링
        #컬럼명__icontains


        if type == 'title' :
            qs = qs.filter(title__icontains=query)
        elif type == 'subject' :
            qs = qs.filter(content__icontains=query)
        else :
            qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query))

# html 파일 앞 디렉토리를 줘서 충돌을 막음

    return render(request, "blog/post_list.html", {
        
        #post_list 값으로 qs 보내줌
        'post_list' : qs,
        'query' : query
    })


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


def post_detail(request, pk) :

    post = Post.objects.get(pk=pk)

    return render(request, 'blog/post_detail.html', {

        'post' : post,
    })


def post_new(request):
     if request.method == 'POST':
        # request.GET
        # request.POST  # POST인자, 파일 제외
         # request.FILES  # POST인자, 파일만
         form = PostForm(request.POST)
         if form.is_valid():
             # form.cleaned_data  # {'title': ??, 'author': ??}
             post = form.save()
             return redirect(post) # post.get_absolute_url()로 이동
         #else:
         #    form.errors
     else:
         # if request.method == 'GET':
         form = PostForm()
     return render(request, 'blog/post_form.html', {
         'form': form,
     })

def post_edit(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
            # request.GET
        # request.POST  # POST인자, 파일 제외
        # request.FILES  # POST인자, 파일만
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # form.cleaned_data  # {'title': ??, 'author': ??}
            post = form.save()
            return redirect('blog:post_detail', post.id)
        #else:
        #    form.errors
    else:
        # if request.method == 'GET':
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def post_delete(request, pk) :

    post = Post.objects.get(pk=pk)


    if request.method == "POST" :
        post.delete()
        return redirect("blog:post_list")

    return render(request, "blog/post_confirm_delete.html", {
        "post" :post,

    })