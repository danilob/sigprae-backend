# Generated by Django 4.1.4 on 2023-01-05 16:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('interestarea', '0016_alter_interestarea_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestarea',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('f1887244-79fb-465d-b0af-c18517d776b7'), editable=False),
        ),
    ]
