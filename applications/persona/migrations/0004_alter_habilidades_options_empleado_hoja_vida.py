# Generated by Django 4.0.3 on 2022-03-17 18:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_empleado_habilidades'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habilidades',
            options={'ordering': ['habilidad'], 'verbose_name': 'Habilidad', 'verbose_name_plural': 'Habilidad Empleados'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
    ]