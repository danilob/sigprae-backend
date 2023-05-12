# Generated by Django 4.1.4 on 2023-01-05 16:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0008_subject_instestareas_alter_subject_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='instestareas',
            new_name='interestareas',
        ),
        migrations.AlterField(
            model_name='subject',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('f18b91e0-1cb3-44f6-bdf6-d275d49fbe2e'), editable=False),
        ),
    ]
