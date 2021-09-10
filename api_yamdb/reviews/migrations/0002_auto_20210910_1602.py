# Generated by Django 2.2.16 on 2021-09-10 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['-text']},
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='genre',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='title',
            name='author',
        ),
        migrations.RemoveField(
            model_name='title',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='title',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='reviews.Category'),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(related_name='genre', to='reviews.Genre'),
        ),
    ]
