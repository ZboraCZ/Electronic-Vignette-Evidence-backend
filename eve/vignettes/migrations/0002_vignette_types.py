import datetime

from django.db import migrations


def create_vignette_types(apps, schema_editor):
    VignetteType = apps.get_model("vignettes", "VignetteType")

    VignetteType(
        name="10denni",
        display_name="10ti denní",
        price=310,
        duration=datetime.timedelta(days=10),
    ).save()

    VignetteType(
        name="30denni",
        display_name="30ti denní",
        price=440,
        duration=datetime.timedelta(days=30),
    ).save()

    VignetteType(
        name="rocni",
        display_name="Roční",
        price=1500,
        duration=datetime.timedelta(days=365),
    ).save()


class Migration(migrations.Migration):

    dependencies = [
        ("vignettes", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_vignette_types),
    ]
