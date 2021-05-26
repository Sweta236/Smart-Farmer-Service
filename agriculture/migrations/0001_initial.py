# Generated by Django 3.1.7 on 2021-05-22 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_agri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order_agri',
            fields=[
                ('userid', models.IntegerField(default=0)),
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.JSONField()),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=20)),
                ('phone', models.CharField(default=' ', max_length=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('payment_id', models.CharField(default='', max_length=50)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='agri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='buy_agri/images')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agriculture.category_agri')),
            ],
        ),
    ]
