# Generated by Django 4.2.1 on 2023-06-02 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_alter_factory_contact_alter_factory_debt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='contact',
            field=models.ManyToManyField(to='supplier.contact'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='product',
            field=models.ManyToManyField(to='supplier.product'),
        ),
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='contact',
            field=models.ManyToManyField(to='supplier.contact'),
        ),
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='product',
            field=models.ManyToManyField(to='supplier.product'),
        ),
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.retailnetwork'),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='contact',
            field=models.ManyToManyField(to='supplier.contact'),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='product',
            field=models.ManyToManyField(to='supplier.product'),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.factory'),
        ),
    ]