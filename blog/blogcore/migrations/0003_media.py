# Generated by Django 3.2.11 on 2022-04-05 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcore', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]