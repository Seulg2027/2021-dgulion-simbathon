# Generated by Django 3.2.3 on 2021-06-23 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerthon', '0002_alter_result_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='demo',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='result',
            name='github',
            field=models.TextField(),
        ),
    ]
