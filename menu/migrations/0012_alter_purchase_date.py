# Generated by Django 4.1.3 on 2023-06-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_alter_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(auto_created=True),
        ),
    ]
