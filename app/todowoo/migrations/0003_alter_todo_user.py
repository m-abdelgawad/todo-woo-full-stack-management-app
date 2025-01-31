# Generated by Django 4.1.4 on 2023-03-10 08:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("todowoo", "0002_alter_todo_datecompleted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="user",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="todos",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
