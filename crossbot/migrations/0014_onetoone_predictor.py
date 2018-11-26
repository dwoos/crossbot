# Generated by Django 2.1.2 on 2018-11-22 05:04

from django.db import migrations, models
import django.db.models.deletion


def set_time(apps, editor):
    Prediction = apps.get_model('crossbot', 'Prediction')
    MiniCrosswordTime = apps.get_model('crossbot', 'MiniCrosswordTime')
    for p in Prediction.objects.all().iterator():
        p.time = MiniCrosswordTime.objects.get(
            user=p.user, date=p.date, seconds__isnull=False, deleted=None
        )
        p.save()


def unset_time(apps, editor):
    Prediction = apps.get_model('crossbot', 'Prediction')
    MiniCrosswordTime = apps.get_model('crossbot', 'MiniCrosswordTime')
    for p in Prediction.objects.all().iterator():
        p.date = p.time.date
        p.user = p.time.user
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('crossbot', '0013_extend_item_keys'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='time',
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='crossbot.MiniCrosswordTime'
            ),
            preserve_default=False,
        ),
        migrations.RunPython(set_time, unset_time),
        migrations.AlterField(
            model_name='prediction',
            name='time',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to='crossbot.MiniCrosswordTime'
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='predictionuser',
            name='user',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to='crossbot.CBUser'
            ),
        ),
        migrations.AlterUniqueTogether(
            name='prediction',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='date',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='user',
        ),
    ]
