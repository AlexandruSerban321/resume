# Generated by Django 2.2.2 on 2020-07-02 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0011_auto_20200702_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='categories',
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='curriculum.Category'),
        ),
    ]