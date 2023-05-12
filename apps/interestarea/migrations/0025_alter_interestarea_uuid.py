

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('interestarea', '0024_alter_interestarea_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestarea',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]
