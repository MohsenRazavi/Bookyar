# Generated by Django 4.1 on 2022-08-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_recommend_alter_comment_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='grade_en',
            field=models.CharField(choices=[('ten', 'دهم'), ('ele', 'یازدهم'), ('twe', 'دوازدهم'), ('alg', 'جامع همه پایه ها'), ('oth', 'دیگر')], default=('oth', 'دیگر'), max_length=3, null=True, verbose_name='پایه'),
        ),
        migrations.AddField(
            model_name='post',
            name='grade_fa',
            field=models.CharField(choices=[('ten', 'دهم'), ('ele', 'یازدهم'), ('twe', 'دوازدهم'), ('alg', 'جامع همه پایه ها'), ('oth', 'دیگر')], default=('oth', 'دیگر'), max_length=3, null=True, verbose_name='پایه'),
        ),
        migrations.AddField(
            model_name='post',
            name='lesson_en',
            field=models.CharField(choices=[('calculus', 'حسابان'), ('physics', 'فیزیک'), ('chemistry', 'شیمی'), ('geometry', 'هندسه'), ('statistics and probability', 'آمار و احتمال'), ('discrete math', 'ریاضیات گسسته'), ('biology', 'زیست'), ('persian', 'فارسی'), ('arabic', 'عربی'), ('english', 'انگلیسی'), ('religion and life', 'دین و زندگی'), ('other', 'دیگر')], default=('other', 'دیگر'), max_length=30, null=True, verbose_name='درس'),
        ),
        migrations.AddField(
            model_name='post',
            name='lesson_fa',
            field=models.CharField(choices=[('calculus', 'حسابان'), ('physics', 'فیزیک'), ('chemistry', 'شیمی'), ('geometry', 'هندسه'), ('statistics and probability', 'آمار و احتمال'), ('discrete math', 'ریاضیات گسسته'), ('biology', 'زیست'), ('persian', 'فارسی'), ('arabic', 'عربی'), ('english', 'انگلیسی'), ('religion and life', 'دین و زندگی'), ('other', 'دیگر')], default=('other', 'دیگر'), max_length=30, null=True, verbose_name='درس'),
        ),
        migrations.AddField(
            model_name='post',
            name='publisher_en',
            field=models.CharField(max_length=200, null=True, verbose_name='انتشارات'),
        ),
        migrations.AddField(
            model_name='post',
            name='publisher_fa',
            field=models.CharField(max_length=200, null=True, verbose_name='انتشارات'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='عنوان'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_fa',
            field=models.CharField(max_length=200, null=True, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(verbose_name='متن مقاله'),
        ),
    ]
