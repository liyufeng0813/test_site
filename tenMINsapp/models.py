from django.db import models
# from faker import Factory
from django.contrib.auth.models import User


class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='profile')
    profile_image = models.FileField(upload_to='profile_image', null=True, blank=True)
    SEX_CHOICES = (
        ('保密', '保密'),
        ('男', '男'),
        ('女', '女'),
    )
    user_sex = models.CharField(choices=SEX_CHOICES, max_length=10)

    def __str__(self):
        return str(self.belong_to)

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.CharField(max_length=300, blank=True)
    cover = models.FileField(upload_to='cover_image', null=True, blank=True)
    views = models.IntegerField(default=0)
    favs = models.IntegerField(default=0)
    createtime = models.DateField(auto_now=True)
    all_choice = models.BooleanField(default=True)
    new_choice = models.BooleanField(default=False)
    editors_choice = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    belong_to = models.ForeignKey(to=Article, related_name='under_comments', blank=True,null=True)
    best_comment = models.BooleanField(default=False)
    def __str__(self):
        return self.content

class Ticket(models.Model):
    voter = models.ForeignKey(to=UserProfile, related_name='voter_ticket')
    article = models.ForeignKey(to=Article, related_name='tickets')
    VOTER_CHOICES = (
        ('like', 'like'),
        ('dislike', 'dislike'),
        ('normal', 'normal')
    )
    choice = models.CharField(choices=VOTER_CHOICES, max_length=10)
    def __str__(self):
        return str(self.id)

# fake = Factory.create()
# for url in range(100):
#     article = Article(
#         title = fake.text(max_nb_chars=90),
#         content = fake.text(max_nb_chars=3000),
#     )
#     article.save()