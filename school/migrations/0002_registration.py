# Generated by Django 3.1.4 on 2020-12-16 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
            ],
        ),
    ]
