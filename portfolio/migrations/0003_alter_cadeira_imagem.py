# Generated by Django 4.0.4 on 2022-05-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_cadeira_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='portfolio\\static\\portfolio\\images\\img_licen'),
        ),
    ]
