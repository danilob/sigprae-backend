# Generated by Django 4.1.4 on 2023-01-12 15:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0012_alter_subject_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]
