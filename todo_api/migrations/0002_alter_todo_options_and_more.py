# Generated by Django 4.1.6 on 2023-02-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['isComplete']},
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='iscompleted',
            new_name='isComplete',
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
