# Generated by Django 3.2 on 2021-04-18 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200426_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitid', models.IntegerField(blank=True, db_column='UnitID', null=True)),
                ('institution', models.TextField()),
                ('state', models.TextField()),
                ('size_category', models.IntegerField()),
                ('urbanization', models.IntegerField()),
                ('city', models.TextField(db_column='City')),
                ('website', models.TextField()),
                ('region', models.IntegerField()),
                ('admission_rate', models.TextField()),
                ('admission_yield', models.TextField()),
                ('finaid_rate', models.TextField()),
                ('tuition_instate', models.TextField()),
                ('tuition_outstate', models.TextField()),
                ('totalstudents', models.IntegerField()),
                ('total_women', models.IntegerField()),
                ('total_asian', models.IntegerField()),
                ('total_black', models.IntegerField()),
                ('total_hispanic', models.IntegerField()),
                ('total_pacific', models.IntegerField()),
                ('student_faculty_ratio', models.TextField()),
            ],
            options={
                'db_table': 'universities',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
    ]
