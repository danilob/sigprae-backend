# Generated by Django 4.1.4 on 2023-01-03 23:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('interestarea', '0004_alter_interestarea_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestarea',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('59539d9d-a55b-4b3c-bfb7-3e8d11a0db9b'), editable=False),
        ),
    ]
