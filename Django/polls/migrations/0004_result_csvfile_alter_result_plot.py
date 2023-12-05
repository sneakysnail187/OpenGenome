# Generated by Django 4.2.7 on 2023-12-05 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_result_plot'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='csvFile',
            field=models.FileField(blank=True, null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='result',
            name='plot',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
