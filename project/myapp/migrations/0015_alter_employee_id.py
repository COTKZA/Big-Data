# Generated by Django 4.1.4 on 2023-02-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0014_alter_employee_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
