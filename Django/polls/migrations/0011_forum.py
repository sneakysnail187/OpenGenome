# Generated by Django 5.0 on 2023-12-07 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_csvnames_csvname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('resultLink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum', to='polls.result')),
            ],
        ),
    ]