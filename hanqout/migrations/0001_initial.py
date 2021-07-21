# Generated by Django 3.2.5 on 2021-07-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hanqout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=50)),
                ('image', models.CharField(default=None, max_length=500)),
                ('description', models.CharField(default=None, max_length=500)),
                ('venue', models.CharField(max_length=200, null=True)),
                ('keywords', models.CharField(max_length=200)),
                ('worth_a_go', models.BooleanField(default=True, null=True)),
            ],
        ),
    ]
