# Generated by Django 3.1.7 on 2021-04-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0002_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='name',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=25),
        ),
    ]
