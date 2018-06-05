# Generated by Django 2.0.3 on 2018-06-04 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=10)),
                ('hgender', models.BooleanField()),
                ('hcontent', models.CharField(max_length=1000)),
                ('isDelete', models.BooleanField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.Bookinfo')),
            ],
        ),
    ]