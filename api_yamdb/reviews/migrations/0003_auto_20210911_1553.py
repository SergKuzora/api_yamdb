# Generated by Django 2.2.16 on 2021-09-11 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210910_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='titles', to='reviews.Category'),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='titles', to='reviews.Genre'),
        ),
    ]
