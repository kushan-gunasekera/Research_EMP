# Generated by Django 3.0.3 on 2020-02-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0002_auto_20200222_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
