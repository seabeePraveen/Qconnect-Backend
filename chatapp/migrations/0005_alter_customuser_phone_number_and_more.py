# Generated by Django 4.2.2 on 2023-06-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatapp", "0004_remove_customuser_is_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="phone_number",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="profile"),
        ),
    ]