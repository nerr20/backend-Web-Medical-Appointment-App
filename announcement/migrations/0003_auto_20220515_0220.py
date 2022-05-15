# Generated by Django 3.2.13 on 2022-05-14 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_category_name2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name2',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[(1, '维护'), (2, '测试'), (3, '节日'), (4, '招募'), (5, '其他')], default='测试', max_length=30, verbose_name='类别'),
        ),
    ]
