from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),  # Зависимость от предыдущей миграции
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Изображение"),
        ),
    ]
