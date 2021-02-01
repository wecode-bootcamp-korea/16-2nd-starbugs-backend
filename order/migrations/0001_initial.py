

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderstatus', to='order.order')),
            ],
            options={
                'db_table': 'orderstatus',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='product.drink')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='order.order')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.size')),
            ],
            options={
                'db_table': 'carts',
            },
        ),
    ]
