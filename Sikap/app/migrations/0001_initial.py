# Generated by Django 3.2.4 on 2021-06-03 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('user_type', models.IntegerField()),
                ('isVerified', models.IntegerField()),
                ('industry', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'Applicant',
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('user_type', models.IntegerField()),
                ('isVerified', models.IntegerField()),
                ('companyName', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Employer',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearsOfExperience', models.IntegerField()),
                ('industry', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('dateadded', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('isAgeViewable', models.IntegerField()),
            ],
            options={
                'db_table': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('user_type', models.IntegerField()),
                ('isVerified', models.IntegerField()),
                ('companyName', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
