# Generated by Django 5.0.6 on 2025-05-13 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosp_app', '0035_alter_ins_pat_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='ins_pat',
            name='amt',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ins_pat',
            name='ins_amt_status',
            field=models.IntegerField(default=0),
        ),
    ]
