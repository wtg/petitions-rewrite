# Generated by Django 2.1.7 on 2019-04-16 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20190303_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petition',
            name='expected_sig',
            field=models.IntegerField(default=250),
        ),
    ]