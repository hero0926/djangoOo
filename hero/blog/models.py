from django.db import models

# Create your models here.


# db생성
# 앱 이름_클래스명 으로 db 생성됨
class Post(models.Model) :
    author = models.CharField(max_length=15)
    # default 지정
    # author = models.CharField(max_length=15, default="어쩌구")
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        # 기본 정렬 설정
        ordering = ['-id']

    def __str__(self):
        # 제목을 리턴
        return self.title
