# Generated by Django 3.2.9 on 2021-11-04 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('tLinkAddr', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('cLinkAddr', models.CharField(max_length=30)),
                ('linkT', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main1.goodstype')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('dateAdded', models.DateField(blank=True, null=True)),
                ('imageLink', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('linkC', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main1.goodscategory')),
                ('linkT', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main1.goodstype')),
            ],
        ),
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gCount', models.DecimalField(decimal_places=2, max_digits=14)),
                ('gSum', models.DecimalField(decimal_places=2, max_digits=14)),
                ('linkG', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main1.goods')),
                ('linkU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]