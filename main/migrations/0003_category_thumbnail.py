# Generated by Django 3.1.1 on 2020-09-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', max_length='100', upload_to='main/categories'),
            preserve_default=False,
        ),
    ]