# Generated by Django 4.1.4 on 2023-01-05 16:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0009_rename_instestareas_subject_interestareas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('41921eb8-7e1b-4575-9cbe-3272c9a966bb'), editable=False),
        ),
    ]
