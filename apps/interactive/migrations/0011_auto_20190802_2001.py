# Generated by Django 2.2.3 on 2019-08-02 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactive', '0010_auto_20190802_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactives',
            name='bible_contents',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='引用经文'),
        ),
    ]
