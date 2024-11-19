# Generated by Django 5.1.3 on 2024-11-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('deadline', models.DateField()),
                ('finished_at', models.DateField(null=True)),
            ],
        ),
    ]
