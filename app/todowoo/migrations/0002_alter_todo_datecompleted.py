# Generated by Django 4.1.4 on 2023-02-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('todowoo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
