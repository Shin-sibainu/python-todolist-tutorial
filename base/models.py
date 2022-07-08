from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    #CASCADEなら関連するモデルも全て削除する。PROTECTなら関連するモデルがあると削除できない
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    title = models.CharField(max_length=200)
    #フォームから投稿するときにこのフィールドの入力は必須ではありません、データベースに保存される値になにも入っていなくても大丈夫です
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["completed"]