# Generated by Django 3.1.4 on 2020-12-11 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_recipe_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientamount',
            old_name='amount',
            new_name='value',
        ),
    ]
