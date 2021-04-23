from rest_framework.authtoken.models import Token
from eve.users.models import Users
from django.db import migrations


def create_users_tokes(apps, schema_editor):
    for user in Users.objects.all():
        Token.objects.get_or_create(user=user)


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_password_hash"),
    ]

    operations = [
        migrations.RunPython(create_users_tokes),
    ]
