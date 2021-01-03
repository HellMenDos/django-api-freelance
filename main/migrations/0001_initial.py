# Generated by Django 3.1.4 on 2021-01-02 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Pass', models.CharField(max_length=30)),
                ('Activate', models.IntegerField()),
                ('Role', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='custmStart', to='main.user')),
                ('Сontractor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contrStart', to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.TextField()),
                ('Seen', models.IntegerField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='custmMessage', to='main.user')),
                ('Сontractor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contrMessage', to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('Message', models.TextField()),
                ('Price', models.IntegerField()),
                ('Status', models.IntegerField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.user')),
            ],
        ),
    ]