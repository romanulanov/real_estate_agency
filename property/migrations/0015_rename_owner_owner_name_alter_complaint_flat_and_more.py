# Generated by Django 4.2.4 on 2023-08-11 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0014_remove_flat_owners_phonenumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.flat', verbose_name='Квартира, на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='сomplainter',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]