# Generated by Django 3.2.4 on 2021-07-15 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TicketsApi', '0003_auto_20210706_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showtimes', to='TicketsApi.cinema'),
        ),
    ]
