# Generated by Django 3.2.7 on 2021-10-03 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20211003_0646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategoryfilterchoice',
            name='subcategory_filter',
        ),
        migrations.DeleteModel(
            name='SubcategoryFilter',
        ),
        migrations.DeleteModel(
            name='SubcategoryFilterChoice',
        ),
    ]
