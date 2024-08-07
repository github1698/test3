# Generated by Django 4.2.3 on 2024-07-16 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_workdoneitem_item_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workdoneitem',
            name='work_list',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.workdonelist'),
        ),
        migrations.AlterField(
            model_name='workdonelist',
            name='title',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.workorder'),
        ),
    ]
