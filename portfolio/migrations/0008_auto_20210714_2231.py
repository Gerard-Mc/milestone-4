# Generated by Django 3.1.13 on 2021-07-14 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20210714_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
    ]
