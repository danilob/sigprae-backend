# Generated by Django 4.1.4 on 2023-01-03 23:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('interestarea', '0007_alter_interestarea_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestarea',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('577c3ee0-97d0-47a7-9dd0-2133d13a4ffb'), editable=False),
        ),
    ]