# Generated by Django 3.2.2 on 2022-03-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20220311_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='book',
            name='num_pages',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='book',
            name='ratings_count',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=50),
        ),
        migrations.AddField(
            model_name='book',
            name='text_reviews_count',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
