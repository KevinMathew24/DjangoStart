# Generated migration file for the Contact model

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=40)),
                ('content', models.TextField()),
            ],
        ),
    ]
