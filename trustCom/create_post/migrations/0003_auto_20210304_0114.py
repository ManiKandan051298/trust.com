# Generated by Django 3.1.7 on 2021-03-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_post', '0002_auto_20210304_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.IntegerField()),
                ('image', models.ImageField(upload_to='frontImage')),
            ],
        ),
        migrations.RemoveField(
            model_name='whatwedo',
            name='heading',
        ),
    ]
