# Generated by Django 4.2.5 on 2023-10-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto1App', '0002_libro_formato'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revista',
            old_name='numpag',
            new_name='numero',
        ),
        migrations.RemoveField(
            model_name='revista',
            name='webpage',
        ),
        migrations.AddField(
            model_name='revista',
            name='fecha_compra',
            field=models.DateField(default='2023-10-16'),
        ),
        migrations.AddField(
            model_name='revista',
            name='fecha_pub',
            field=models.DateField(default='2023-10-16'),
        ),
        migrations.AddField(
            model_name='revista',
            name='formato',
            field=models.CharField(choices=[('digital', 'Digital'), ('fisica', 'Física')], default='fisica', max_length=20),
        ),
        migrations.AddField(
            model_name='revista',
            name='titulo',
            field=models.CharField(default='revista1', max_length=40),
        ),
        migrations.AddField(
            model_name='revista',
            name='web',
            field=models.CharField(default='página web', max_length=40),
        ),
    ]