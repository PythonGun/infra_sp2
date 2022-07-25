# Generated by Django 2.2.16 on 2022-05-15 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20220515_2320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveConstraint(
            model_name='user',
            name='confirm-user-unuque',
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
    ]
