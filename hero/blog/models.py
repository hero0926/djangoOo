from django.db import models
import os
import uuid;
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your models here.


# db생성
# 앱 이름_클래스명 으로 db 생성됨
class Post(models.Model) :
    # default 지정
    # author = models.CharField(max_length=15, default="어쩌구")


    def min_length_name(value):
        if len(value) < 2:
            raise ValidationError("두글자 이상 입력하세요")

    author = models.CharField(max_length=15, validators=[min_length_name])
    title = models.CharField(max_length=100, help_text="이름을 넣어주세요", validators=[min_length_name])
    content = models.TextField(help_text="markdown 문법 지원")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        # 기본 정렬 설정
        ordering = ['-id']

    def __str__(self):
        # 제목을 리턴
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])



def random_upload_to(instance, orig_filename) :

    ext = os.path.splitext(orig_filename)[-1].lower()
    filename = uuid.uuid4().hex + ext
    filepath = os.path.join(filename[:3], filename[3:6], filename[6:9], filename[9:])

    return filepath

