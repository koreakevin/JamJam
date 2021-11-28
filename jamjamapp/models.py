from django.db import models
from django.conf import settings
from functools import update_wrapper
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.utils import timezone
from django.urls import reverse

# 게시글


class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Writer = models.CharField(max_length=100)
    Write_day = models.DateTimeField('date published')
    Content = models.TextField()
    Image = models.ImageField(upload_to='images/', blank=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    Blog_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Blog_likes")
    view_count = models.IntegerField(default=0)

    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_post', blank=True)
    favorite = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorite_post', blank=True)

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['-id']

# 댓글

class Comment(models.Model):
    post_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published', null = True)
    
    def __str__(self):
        return self.text

# 커뮤니티 카테고리를 해시태그라고 편의상 해둠


class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# course_eat_C


class Eat_C(models.Model):
    Title = models.CharField(max_length=200)
    Writer = models.CharField(max_length=100)
    Write_day = models.DateTimeField('date published')
    Content = models.TextField()
    Image = models.ImageField(upload_to='images/', blank=True)
    big_region = models.ManyToManyField('big_region', blank=True)
    small_region = models.ManyToManyField('small_region', blank=True)
    Eat_likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="Eat_likes")
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.Title

# course_look_C


class Look_C(models.Model):
    Title = models.CharField(max_length=200)
    Writer = models.CharField(max_length=100)
    Write_day = models.DateTimeField('date published')
    Content = models.TextField()
    Image = models.ImageField(upload_to='images/', blank=True)
    big_region = models.ManyToManyField('big_region', blank=True)
    small_region = models.ManyToManyField('small_region', blank=True)
    Look_likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="Look_likes")
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.Title

# course_play_C


class Play_C(models.Model):
    Title = models.CharField(max_length=200)
    Writer = models.CharField(max_length=100)
    Write_day = models.DateTimeField('date published')
    Content = models.TextField()
    Image = models.ImageField(upload_to='images/', blank=True)
    big_region = models.ManyToManyField('big_region', blank=True)
    small_region = models.ManyToManyField('small_region', blank=True)
    play_likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="Play_likes")
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.Title


class Big_Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Small_Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# 스크랩


class Bookmark(models.Model):
    book_site_name = models.CharField(max_length=50)
    book_url = models.URLField()

    def __str__(self):
        return self.book_site_name + " : " + self.book_url

    class Meta:
        ordering = ["book_site_name"]


# 다이어리
class Event(models.Model):
    diary_start_time = models.DateTimeField("시작시간")
    diary_end_time = models.DateTimeField("마감시간")
    diary_title = models.CharField("이벤트 이름", max_length=50)
    diary_description = models.TextField("상세")

    class Meta:
        verbose_name = "이벤트 데이터"
        verbose_name_plural = "이벤트 데이터"

    def __str__(self):
        return self.diary_title

    @property
    def get_html_url(self):
        diary_url = reverse('edit', args=(self.id,))
        return f'<a href="{diary_url}"> {self.diary_title} </a>'


# ----민정이 개발 부분------


class Post(models.Model):
    diary_title = models.CharField(max_length=100)  # 제목
    # 기록하고 싶은 날짜( ex) 여행 다녀온 날 등 )
    diary_date = models.CharField(
        null=False, max_length=15, default='oooo년 oo월 oo일')
    diary_body = models.TextField()  # 내용

    def __str__(self):
        return self.diary_title

# 버킷리스트 모델


class Bucket(models.Model):
    bucket_title = models.CharField(max_length=100)  # 제목
    bucket_date = models.CharField(
        null=False, max_length=15, default='oooo년 oo월 oo일')  # 하고 싶은 날짜( ex) ~날 ~하기 등 )
    bucket_body = models.TextField()  # 내용

    def __str__(self):
        return self.bucket_title

# 프로필 모델


class Profile(models.Model):
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname

# ----예찬이 개발 부분------


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('이메일을 입력해주세요')
        if not password:
            raise ValueError('비밀번호를 입력해주세요')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class SettingUser(AbstractBaseUser, PermissionsMixin):
    g = [
        (1, '성별'),
        (2, '남성'),
        (3, '여성')
    ]

    objects = UserManager()
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=20, unique=True, null=True)
    nickname = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(default="010", max_length=11, null=True)
    birthyear = models.CharField(max_length=4, null=True)
    birthmonth = models.CharField(max_length=2, null=True)
    birthday = models.CharField(max_length=2, null=True)
    gender = models.IntegerField(default=1, choices=g, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.username)
