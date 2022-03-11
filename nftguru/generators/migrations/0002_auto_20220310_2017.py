# Generated by Django 3.2.12 on 2022-03-10 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('generators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='layer',
            field=models.ForeignKey(default=423, on_delete=django.db.models.deletion.CASCADE, related_name='layer_name', to='generators.layer'),
        ),
    ]
