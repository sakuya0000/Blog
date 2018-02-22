from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()

    def __unicode__(self):
        return self.username


class Category(models.Model):
    name = models.CharField('名称', max_length=20)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('内容')
    pub = models.DateField('发布时间', auto_now_add=True)#添加时自动加入现在时间
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)#外键与Category表相连,多对一（博客--类别）

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='博客', on_delete=models.CASCADE)#(博客--评论:一对多)
    name = models.CharField('称呼', max_length=16)
    content = models.CharField('内容', max_length=240)
    pub = models.DateField('发布时间', auto_now_add=True)

    def __unicode__(self):
        return self.content
