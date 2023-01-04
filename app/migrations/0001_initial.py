# Generated by Django 4.1.4 on 2022-12-27 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('item_name', models.TextField()),
                ('item_description', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
