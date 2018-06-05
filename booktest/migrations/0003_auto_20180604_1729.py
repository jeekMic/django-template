# Generated by Django 2.0.3 on 2018-06-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_heroinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heroinfo',
            old_name='book',
            new_name='hbook',
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hcontent',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hgender',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
    ]
