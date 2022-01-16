# Generated by Django 3.1.3 on 2022-01-16 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PricePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=2)),
                ('sugang_type', models.CharField(max_length=2)),
                ('price', models.IntegerField()),
                ('refund', models.IntegerField()),
                ('start_dt', models.CharField(max_length=8)),
                ('end_dt', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=2)),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sugang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=1)),
                ('day', models.IntegerField()),
                ('time', models.IntegerField()),
                ('start_dt', models.CharField(max_length=8)),
                ('end_dt', models.CharField(max_length=8)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyroom.student')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer', models.CharField(max_length=40)),
                ('pay_type', models.CharField(max_length=1)),
                ('brother_dc_yn', models.CharField(blank=True, max_length=1, null=True)),
                ('recommend_dc_start', models.CharField(blank=True, max_length=8, null=True)),
                ('recommend_dc_end', models.CharField(blank=True, max_length=8, null=True)),
                ('create_date', models.DateTimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyroom.student')),
                ('substudent', models.ManyToManyField(blank=True, null=True, related_name='student_brother', to='studyroom.Student')),
            ],
        ),
    ]
