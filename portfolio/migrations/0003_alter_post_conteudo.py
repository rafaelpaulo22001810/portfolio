# Generated by Django 4.0.4 on 2022-06-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_cadeira_classificacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=models.TextField(max_length=500),
        ),
    ]