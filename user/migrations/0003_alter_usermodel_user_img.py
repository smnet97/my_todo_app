# Generated by Django 4.2.2 on 2023-06-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_usermodel_user_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="user_img",
            field=models.ImageField(
                default="../static/main/img/user.png", upload_to="user/"
            ),
        ),
    ]
