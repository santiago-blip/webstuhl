# Generated by Django 4.1.1 on 2022-10-20 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_prospects_remove_users_waiting_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='prospect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.prospects'),
        ),
    ]
