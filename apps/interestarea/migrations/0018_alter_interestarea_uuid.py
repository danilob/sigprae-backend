# Generated by Django 4.1.4 on 2023-01-10 17:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('interestarea', '0017_alter_interestarea_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestarea',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('974cbb62-fc85-4dc5-83e4-9bf1bbfa6b70'), editable=False),
        ),
    ]
