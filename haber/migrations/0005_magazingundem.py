# Generated by Django 4.2.4 on 2023-10-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haber', '0004_alter_haber_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='magazinGundem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50, verbose_name='Ünlü İsmi')),
                ('resim', models.ImageField(upload_to=None, verbose_name='Ünlü Resim')),
            ],
        ),
    ]