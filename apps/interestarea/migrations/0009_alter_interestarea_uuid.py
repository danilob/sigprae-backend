# Generated by Django 4.1.4 on 2023-01-03 23:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('interestarea', '0008_alter_interestarea_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestarea',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('2c84b5af-96dc-4163-be17-b54b05abaa24'), editable=False),
        ),
    ]
