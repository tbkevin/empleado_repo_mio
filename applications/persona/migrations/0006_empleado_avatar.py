# Generated by Django 4.0.3 on 2022-04-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_alter_empleado_options_remove_empleado_hoja_vida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
