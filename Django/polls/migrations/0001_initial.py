# Generated by Django 4.2.7 on 2023-12-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.CharField(max_length=30)),
                ('experimentTitle', models.CharField(max_length=200)),
                ('targetGenes', models.CharField(max_length=200)),
                ('experimentNotes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Plots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot', models.ImageField(upload_to='')),
            ],
        ),
    ]
