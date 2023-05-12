# Generated by Django 4.1.4 on 2023-01-05 16:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('interestarea', '0015_alter_interestarea_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestarea',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('6a102ae6-b66e-4588-9068-54bb0c773a09'), editable=False),
        ),
    ]