# Generated by Django 4.1.3 on 2023-06-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_alter_purchase_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='date',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='rupees',
            field=models.IntegerField(),
        ),
    ]