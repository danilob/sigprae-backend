# Generated by Django 4.1.4 on 2023-01-03 23:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('interestarea', '0011_alter_interestarea_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestarea',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('c36be9fd-628a-4732-92ef-cc4dc23c87e4'), editable=False),
        ),
    ]