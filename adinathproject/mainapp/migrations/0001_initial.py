# Generated by Django 3.1.4 on 2020-12-25 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_data', models.FileField(upload_to='order_documents/')),
                ('order_completed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=2000)),
                ('product_description', models.TextField()),
                ('product_old_prize', models.PositiveIntegerField()),
                ('product_prize', models.PositiveIntegerField()),
                ('productimage_1', models.ImageField(upload_to='')),
                ('productimage_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('productimage_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('productimage_4', models.ImageField(blank=True, null=True, upload_to='')),
                ('productimage_5', models.ImageField(blank=True, null=True, upload_to='')),
                ('productimage_6', models.ImageField(blank=True, null=True, upload_to='')),
                ('productimage_7', models.ImageField(blank=True, null=True, upload_to='')),
                ('productimage_8', models.ImageField(blank=True, null=True, upload_to='')),
                ('productimage_9', models.ImageField(blank=True, null=True, upload_to='')),
                ('productimage_10', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_sub_category', models.CharField(max_length=200)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
        ),
    ]
