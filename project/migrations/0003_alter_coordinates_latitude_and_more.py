# Generated by Django 5.1.3 on 2024-11-22 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinates',
            name='latitude',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='longitude',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='images',
            name='data',
            field=models.ImageField(blank=True, null=True, upload_to='media/pereval/'),
        ),
    ]
