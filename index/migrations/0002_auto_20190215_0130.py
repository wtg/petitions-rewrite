# Generated by Django 2.1.1 on 2019-02-15 01:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("index", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="petition",
            name="created_date",
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime(2019, 2, 15, 1, 30, 44, 768987, tzinfo=utc),
            ),
        ),
        migrations.AlterField(
            model_name="signature",
            name="signed_date",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 2, 15, 1, 30, 44, 767805, tzinfo=utc)
            ),
        ),
    ]