import datetime

from django.db import migrations
from eve.roles.models import Roles


def create_users(apps, schema_editor):
    Users = apps.get_model("users", "Users")

    Users(
        email="admin@znamky.com",
        first_name="FS_Admin",
        last_name="LS_Admin",
        password="aaaaa",
        phone="666666666",
        role_id=1
    ).save()

    Users(
        email="user@znamky.com",
        first_name="Milan",
        last_name="Chrápal",
        password="aaaaa",
        phone="777777777",
        role_id=2
    ).save()


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]
