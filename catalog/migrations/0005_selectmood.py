# Generated by Django 3.0.5 on 2020-06-10 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200526_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectMood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(blank=True, choices=[('g', 'good'), ('b', 'bad')], default='b', help_text='Select the mood', max_length=1)),
            ],
        ),
    ]
