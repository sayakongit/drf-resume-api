# Generated by Django 4.1.1 on 2022-09-23 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('Bihar', 'Bihar'), ('Jharkhand', 'Jharkhand'), ('West Bengal', 'West Bengal')], max_length=50)),
                ('gender', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pimage', models.ImageField(blank=True, upload_to='pimages')),
                ('rdoc', models.ImageField(blank=True, upload_to='rdocs')),
            ],
        ),
    ]
