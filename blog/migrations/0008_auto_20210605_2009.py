# Generated by Django 3.1.7 on 2021-06-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='quote',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='sub_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
