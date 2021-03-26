import datetime

from django.db import migrations


def create_roles(apps, schema_editor):
    Roles = apps.get_model("roles", "Roles")

    Roles(
        id=1,
        name="admin",
    ).save()

    Roles(
        id=2,
        name="user",
    ).save()


class Migration(migrations.Migration):

    dependencies = [
        ("roles", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_roles),
    ]
