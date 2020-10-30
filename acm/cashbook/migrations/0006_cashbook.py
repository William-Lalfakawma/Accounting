# Generated by Django 3.1.2 on 2020-10-29 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbook', '0005_auto_20201029_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashBook',
            fields=[
                ('sl_no', models.AutoField(primary_key=True, serialize=False)),
                ('credit_or_debit', models.CharField(choices=[('credit', 'credit'), ('debit', 'debit')], default='debit', max_length=20)),
                ('bank_or_cash', models.CharField(choices=[('cash', 'cash'), ('bank', 'bank')], default='cash', max_length=20)),
                ('particulars', models.CharField(default=False, max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remarks', models.TextField(blank=True)),
            ],
        ),
    ]