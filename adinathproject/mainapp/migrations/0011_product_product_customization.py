# Generated by Django 3.1.4 on 2020-12-30 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20201227_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_customization',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5, null=True),
        ),
    ]
