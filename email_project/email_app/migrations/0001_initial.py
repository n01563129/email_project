# Generated by Django 5.0.4 on 2024-04-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=254)),
                ('receiver', models.EmailField(max_length=254)),
                ('cc', models.CharField(blank=True, max_length=1000)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
            ],
        ),
    ]
