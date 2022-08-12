# Generated by Django 3.2.12 on 2022-03-30 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo1', '0002_auto_20220329_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('priority', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='todo',
        ),
    ]