# Generated by Django 4.2.21 on 2025-07-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_client",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_company",
        ),
        migrations.AddField(
            model_name="user",
            name="account_type",
            field=models.CharField(
                choices=[("client", "عميل"), ("company", "شركه")],
                default="client",
                max_length=10,
                verbose_name="نوع الحساب",
            ),
        ),
    ]
