# Generated by Django 3.1.4 on 2020-12-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20201205_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='Изображение'),
        ),
    ]