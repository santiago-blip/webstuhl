# Generated by Django 4.1.1 on 2022-10-26 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguagesLevels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_level', models.CharField(max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='languages',
            name='language_level',
        ),
        migrations.CreateModel(
            name='LanguagesLanguagesLevels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.languages')),
                ('language_level_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.languageslevels')),
            ],
        ),
    ]