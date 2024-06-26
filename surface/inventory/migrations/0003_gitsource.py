# Generated by Django 3.2.23 on 2024-05-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_finding'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_url', models.URLField(max_length=628)),
                ('branch', models.CharField(default='master', max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('manually_inserted', models.BooleanField(default=False)),
                ('apps', models.ManyToManyField(blank=True, to='inventory.Application', verbose_name='Application')),
            ],
            options={
                'verbose_name': 'Git Source',
                'unique_together': {('repo_url', 'branch')},
            },
        ),
    ]
