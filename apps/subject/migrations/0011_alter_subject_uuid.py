# Generated by Django 4.1.4 on 2023-01-10 17:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0010_alter_subject_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('43c68429-9cca-4413-8d89-2592e4a3f70a'), editable=False),
        ),
    ]
