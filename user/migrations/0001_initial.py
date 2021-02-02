# Generated by Django 3.1.4 on 2021-02-02 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('density', models.IntegerField(default=0)),
                ('taste', models.IntegerField(default=0)),
                ('feel', models.IntegerField(default=0)),
                ('drink_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.drinkstatus')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
