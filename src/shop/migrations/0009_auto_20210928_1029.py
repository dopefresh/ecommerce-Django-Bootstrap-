# Generated by Django 3.2.7 on 2021-09-28 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210928_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_steps',
        ),
        migrations.AlterField(
            model_name='orderstep',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_steps', to='shop.order', verbose_name='order'),
        ),
    ]
