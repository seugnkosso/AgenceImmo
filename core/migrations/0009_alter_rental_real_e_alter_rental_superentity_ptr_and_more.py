# Generated by Django 5.1.2 on 2024-10-14 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_rental_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='real_e',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.real_estate'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='superentity_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.superentity'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.tenant'),
        ),
    ]
