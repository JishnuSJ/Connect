# Generated by Django 5.0.6 on 2025-05-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosp_app', '0028_ins_pat'),
    ]

    operations = [
        migrations.AddField(
            model_name='ins_pat',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
