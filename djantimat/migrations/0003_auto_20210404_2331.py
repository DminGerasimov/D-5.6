# Generated by Django 3.1.7 on 2021-04-04 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djantimat', '0002_auto_20210319_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slang',
            options={'verbose_name': 'Нецезурное слово', 'verbose_name_plural': 'Нецензурные слова'},
        ),
        migrations.AlterField(
            model_name='slang',
            name='word',
            field=models.CharField(help_text='Можете вписать любое слово - оно будет нормализовано автоматически', max_length=64, unique=True, verbose_name='Нормальная форма слова ненормативной лексики'),
        ),
    ]
