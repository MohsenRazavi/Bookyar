# Generated by Django 4.1 on 2022-08-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='need_or_add',
            field=models.CharField(blank=True, choices=[('need', 'needed'), ('add', 'added')], max_length=5),
        ),
    ]