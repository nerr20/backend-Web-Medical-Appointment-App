from django.db import models
from django.utils import timezone


class Announcement(models.Model):
    title = models.CharField('标题', max_length=70)
    author = models.CharField('作者', max_length=30)
    created_time = models.DateTimeField('发布时间', default=timezone.now)
    modified_time = models.DateTimeField('最近修改时间')
    types = (
        ('维护', '维护'),
        ('测试', '测试'),
        ('节日', '节日'),
        ('招募', '招募'),
        ('其他', '其他'),
    )
    category = models.CharField('分类', choices=types, max_length=30)
    body = models.TextField('正文')

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = verbose_name
        ordering = ['-created_time', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)