from random import choices
from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField

# Create your models here.

class Calendar(models.Model): # 대시보드 캘린더 모델
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    startday = models.DateField(null=True)
    endday = models.DateField(null=True)
    starttime = models.TimeField(null=True)
    endtime = models.TimeField(null=True)
    place = models.CharField(max_length=20)
    body = models.TextField()

    COLOR_PALETTE = [
        ("#50cfbc","1",),("#fe7782","2",),("#45bfff","3",),("#ffbc54","4",),("#735bf2","5",),
        ]
    color = ColorField(samples=COLOR_PALETTE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]
    
    class Meta:
        verbose_name = "캘린더"
        verbose_name_plural = "캘린더(들)"
# 캘린더 모델을 다룰거다라는 request를 보냄 but 반영이 안돼서 에러가뜸
# no such column 은 migrations 오류임

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateField() # 시간이 필요 없어서 변경함
    body = models.TextField()


# 프로젝트 관리에서 받아오기 떄문에 필요 없음 
# class TodoTitle(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=200)
#     user = models.ForeignKey(User,on_delete=models.CASCADE) # 외래키를 유저 모델과 연동하겠다. 유저객체가 삭제됐을 때 연동된 객체를 같이 삭제하겠다
    # on_delete 설정을 안하면 그대로 남게된다. 네이버 지식인 같은 것임
    # 만약 온딜리트 설정을 해놨다면 회원탈퇴시 같이 삭제되는 것임 

class Todo(models.Model):
    content = models.TextField()
    project = models.ForeignKey(Project ,on_delete=models.CASCADE, related_name='todos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.post
    
    # def todocomment(self):
    #     return self.post