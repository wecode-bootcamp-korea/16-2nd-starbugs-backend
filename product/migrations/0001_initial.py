

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'allergies',
            },
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_name', models.CharField(max_length=50)),
                ('english_name', models.CharField(max_length=50)),
                ('main_description', models.TextField()),
                ('sub_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_new', models.BooleanField()),
                ('is_season', models.BooleanField()),
                ('density', models.IntegerField(default=0)),
                ('taste', models.IntegerField(default=0)),
                ('feel', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('image_url', models.URLField()),
            ],
            options={
                'db_table': 'drinks',
            },
        ),
        migrations.CreateModel(
            name='DrinkStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'drinkstatus',
            },
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'maincategories',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200, null=True)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='product.maincategory')),
            ],
            options={
                'db_table': 'subcategories',
            },
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kcal', models.IntegerField()),
                ('sodium', models.IntegerField()),
                ('saturation', models.IntegerField()),
                ('sugar', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('caffeine', models.IntegerField()),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutritions', to='product.drink')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutritions', to='product.size')),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='DrinkAllergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.allergy')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.drink')),
            ],
            options={
                'db_table': 'drinkallergies',
            },
        ),
        migrations.AddField(
            model_name='drink',
            name='allergies',
            field=models.ManyToManyField(through='product.DrinkAllergy', to='product.Allergy'),
        ),
        migrations.AddField(
            model_name='drink',
            name='drink_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='product.drinkstatus'),
        ),
        migrations.AddField(
            model_name='drink',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='product.subcategory'),
        ),
    ]
