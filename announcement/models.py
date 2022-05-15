from django.db import models
from django.utils import timezone


class Announcement(models.Model):
    title = models.CharField('标题', max_length=70, help_text='公告标题')
    author = models.CharField('作者', max_length=30, help_text='公告作者')
    created_time = models.DateTimeField('发布时间', default=timezone.now, help_text='公告创建时间')
    modified_time = models.DateTimeField('最近修改时间', help_text='公告最近修改时间')
    types = (
        ('系统维护', '系统维护'),
        ('信息更新', '信息更新'),
        ('节日假期', '节日假期'),
        ('人员招募', '人员招募'),
        ('其他', '其他'),
    )
    category = models.CharField('分类', choices=types, max_length=30, help_text='公告类型')
    body = models.TextField('正文', help_text='公告正文')

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = verbose_name
        ordering = ['-created_time', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

