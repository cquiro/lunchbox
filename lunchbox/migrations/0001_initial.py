# Generated by Django 2.0.7 on 2018-08-06 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lunchbox.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferences', models.CharField(max_length=200)),
                ('size', models.CharField(choices=[('XL', 'Extra Large'), ('NL', 'Normal')], default=lunchbox.models.Sizes('Normal'), max_length=2)),
                ('eater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='menu date')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunchbox.Menu')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunchbox.Option'),
        ),
    ]