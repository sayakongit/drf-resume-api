# Generated by Django 4.1.1 on 2022-09-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rdoc',
            field=models.FileField(blank=True, upload_to='rdocs'),
        ),
    ]