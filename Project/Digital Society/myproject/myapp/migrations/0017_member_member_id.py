# Generated by Django 3.2.3 on 2022-07-14 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_member_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]
