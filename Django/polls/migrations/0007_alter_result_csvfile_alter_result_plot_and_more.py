# Generated by Django 4.2.7 on 2023-12-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_usercsv_csv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='csvFile',
            field=models.FileField(blank=True, null=True, upload_to='ResultsCSV'),
        ),
        migrations.AlterField(
            model_name='result',
            name='plot',
            field=models.ImageField(blank=True, null=True, upload_to='Plots'),
        ),
        migrations.AlterField(
            model_name='usercsv',
            name='csv',
            field=models.FileField(blank=True, null=True, upload_to='SubmittedCSV'),
        ),
    ]
