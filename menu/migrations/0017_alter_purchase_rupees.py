# Generated by Django 4.1.3 on 2023-06-25 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_alter_purchase_rupees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='rupees',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
