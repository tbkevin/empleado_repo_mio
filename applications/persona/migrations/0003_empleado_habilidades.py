# Generated by Django 4.0.3 on 2022-03-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_habilidades_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.habilidades'),
        ),
    ]
