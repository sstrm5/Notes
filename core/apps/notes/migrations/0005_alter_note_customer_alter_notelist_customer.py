# Generated by Django 5.1.3 on 2024-11-26 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_alter_customer_expires_in_and_more'),
        ('notes', '0004_alter_notelist_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='customers.customer', verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='notelist',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_list', to='customers.customer', verbose_name='Пользователь'),
        ),
    ]
