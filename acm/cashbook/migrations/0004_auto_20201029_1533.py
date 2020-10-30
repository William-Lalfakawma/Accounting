# Generated by Django 3.1.2 on 2020-10-29 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashbook', '0003_auto_20201029_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daybook',
            name='ledger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ledger_master_name', to='cashbook.ledgermaster'),
        ),
        migrations.AlterField(
            model_name='ledger',
            name='ledger_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='last_ledger_name', to='cashbook.daybook'),
        ),
    ]
