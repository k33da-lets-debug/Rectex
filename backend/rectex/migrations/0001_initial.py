# Generated by Django 3.1.3 on 2020-11-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OCR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_be_converted_image', models.ImageField(upload_to='raw_images/')),
            ],
        ),
    ]