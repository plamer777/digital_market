# Generated by Django 4.2.1 on 2023-06-01 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=50)),
                ('home_number', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('debt', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ManyToManyField(to='supplier.contact')),
            ],
            options={
                'verbose_name': 'Фабрика',
                'verbose_name_plural': 'Фабрики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='RetailNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('debt', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ManyToManyField(to='supplier.contact')),
                ('product', models.ManyToManyField(to='supplier.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplier.factory')),
            ],
            options={
                'verbose_name': 'Розничная сеть',
                'verbose_name_plural': 'Розничные сети',
            },
        ),
        migrations.CreateModel(
            name='IndividualEntrepreneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('debt', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ManyToManyField(to='supplier.contact')),
                ('product', models.ManyToManyField(to='supplier.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplier.retailnetwork')),
            ],
            options={
                'verbose_name': 'Индивидуальный предприниматель',
                'verbose_name_plural': 'Индивидуальные предприниматели',
            },
        ),
        migrations.AddField(
            model_name='factory',
            name='product',
            field=models.ManyToManyField(to='supplier.product'),
        ),
    ]
