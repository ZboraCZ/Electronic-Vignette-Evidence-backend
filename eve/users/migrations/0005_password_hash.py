import datetime
import hashlib

from django.db import migrations
from eve.roles.models import Roles


def create_users(apps, schema_editor):
    Users = apps.get_model("users", "Users")

    user1 = Users.objects.get(email="admin@znamky.com")
    user1.password = hashlib.sha256(user1.password.encode()).hexdigest()
    user1.save()

    user2 = Users.objects.get(email="user@znamky.com")
    user2.password = hashlib.sha256(user2.password.encode()).hexdigest()
    user2.save()


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_auto_20210419_1637"),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]
