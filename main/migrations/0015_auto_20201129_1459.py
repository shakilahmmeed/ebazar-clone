# Generated by Django 3.1.1 on 2020-11-29 08:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_merge_20201129_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='sub_tagline',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='facebook',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='instagram',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='youtube',
            field=models.CharField(max_length=50),
        ),
    ]
