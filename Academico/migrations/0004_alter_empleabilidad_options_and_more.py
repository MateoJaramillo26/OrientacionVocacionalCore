# Generated by Django 5.2.1 on 2025-06-01 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0003_remove_universidad_empleabilidad_empleabilidad_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleabilidad',
            options={'verbose_name': 'Empleabilidad', 'verbose_name_plural': 'Empleabilidad'},
        ),
        migrations.AlterModelOptions(
            name='investigacionydescubrimiento',
            options={'verbose_name': 'Investigación y Descubrimiento', 'verbose_name_plural': 'Investigación y Descubrimientos'},
        ),
    ]
