# Generated by Django 5.0.7 on 2024-08-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0004_alter_customuser_tc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tc',
            field=models.BooleanField(default=True),
        ),
    ]
