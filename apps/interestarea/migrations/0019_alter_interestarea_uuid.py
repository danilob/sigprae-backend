# Generated by Django 4.1.4 on 2023-01-09 23:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('interestarea', '0018_alter_interestarea_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestarea',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('bbf25b59-3885-4f63-9df5-533b7a9ce943'), editable=False),
        ),
    ]
