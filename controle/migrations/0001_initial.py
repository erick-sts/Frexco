# Generated by Django 4.1.3 on 2022-11-14 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('nascimento', models.DateField()),
            ],
        ),
    ]
