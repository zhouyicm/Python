from datetime import datetime

from django.db import models


# Create your models here.


class Course(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=u'课程名称'
    )
    desc = models.CharField(
        max_length=300,
        verbose_name=u'课程描述'
    )
    detail = models.TextField(
        verbose_name=u'课程详情'
    )
    degree = models.CharField(
        choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', u'高级')),
        max_length=5,
        verbose_name=u'难度'
    )
    leran_times = models.IntegerField(
        default=0,
        verbose_name=u'学习时长（分钟）'
    )
    students = models.IntegerField(
        default=0,
        verbose_name=u'学习人数'
    )
    fav_nums= models.IntegerField(
        default=0,
        verbose_name=u'收藏人数'
    )
    image = models.ImageField(
        upload_to='scourses/%Y/%m',
        verbose_name=u'封面'
    )
    chick_nums = models.IntegerField(
        default=0,
        verbose_name=u'点击数'
    )
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name=u'添加时间'
    )

    # 重载Unicode/__str__方法以显示正确的title
    def __str__(self):
        return ('{0}:{1}'.format(self.name, self.degree))

    class Meta:
        verbose_name=u'课程'
        verbose_name_plural=verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL, verbose_name=u'课程')
    name = models.CharField(
        max_length=100,
        verbose_name=u'章节名'
    )
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name=u'添加时间'
    )


    # 重载Unicode/__str__方法以显示正确的title
    def __str__(self):
        return ('{0}'.format(self.name))

    class Meta:
        verbose_name=u'章节'
        verbose_name_plural=verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, null=True, on_delete=models.SET_NULL, verbose_name=u'章节')
    name = models.CharField(
        max_length=100,
        verbose_name=u'视频名称'
    )
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name=u'添加时间'
    )

    # 重载Unicode/__str__方法以显示正确的title
    def __str__(self):
        return ('{0}'.format(self.name))

    class Meta:
        verbose_name=u'视频'
        verbose_name_plural=verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL, verbose_name=u'课程')
    name = models.CharField(
        max_length=100,
        verbose_name=u'视频名称'
    )
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name=u'添加时间'
    )
    dawnload = models.FileField(
        upload_to='course/resource/%Y/%m',
        max_length=100
    )

    # 重载Unicode/__str__方法以显示正确的title
    def __str__(self):
        return ('{0}'.format(self.name))

    class Meta:
        verbose_name=u'课程资源'
        verbose_name_plural=verbose_name