# Generated by Django 4.0.3 on 2022-03-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_alter_habilidades_options_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['id'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Recursos humanos'},
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='hoja_vida',
        ),
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=60, verbose_name='Nombre completo'),
        ),
    ]
