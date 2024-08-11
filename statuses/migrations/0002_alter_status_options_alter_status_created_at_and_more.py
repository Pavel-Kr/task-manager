# Generated by Django 5.0.7 on 2024-08-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'status', 'verbose_name_plural': 'statuses'},
        ),
        migrations.AlterField(
            model_name='status',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation time'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='status',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Last update time'),
        ),
    ]
