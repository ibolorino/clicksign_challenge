# Generated by Django 4.1.1 on 2022-09-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_folder_parent_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='level',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nível da Pasta'),
        ),
        migrations.AlterUniqueTogether(
            name='folder',
            unique_together={('name', 'level')},
        ),
    ]