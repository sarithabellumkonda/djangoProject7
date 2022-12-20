# Generated by Django 4.1.4 on 2022-12-19 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=20)),
                ('pcost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pmfdt', models.DateField()),
                ('pexpdt', models.DateField()),
            ],
        ),
    ]
