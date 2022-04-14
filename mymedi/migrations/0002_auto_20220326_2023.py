# Generated by Django 3.2.8 on 2022-03-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymedi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('phn_no', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField(unique=True)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=20)),
                ('phn_no', models.BigIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.IntegerField(unique=True)),
                ('mname', models.CharField(max_length=30)),
                ('dname', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=30)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('phn_no', models.BigIntegerField()),
                ('price', models.BigIntegerField()),
                ('qty', models.BigIntegerField()),
                ('total', models.BigIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='dealer',
            name='phone',
            field=models.PositiveBigIntegerField(unique=True),
        ),
    ]