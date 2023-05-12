

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0017_alter_subject_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]
