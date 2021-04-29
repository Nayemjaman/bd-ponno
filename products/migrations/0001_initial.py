# Generated by Django 3.1.7 on 2021-04-29 05:42

import django.core.validators
from django.db import migrations, models
import djongo.models.fields
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('product_url', models.URLField(validators=[django.core.validators.URLValidator])),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('image_url', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator])),
                ('in_stock', models.IntegerField(blank=True, default=0, null=True)),
                ('tags', djongo.models.fields.ArrayField(model_container=products.models.Tag, model_form_class=products.models.TagForm)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', djongo.models.fields.ArrayReferenceField(blank=True, on_delete=djongo.models.fields.ArrayReferenceField._on_delete, related_name='products', to='products.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='products_product_name_index'),
        ),
    ]
