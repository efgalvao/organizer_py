# Generated by Django 5.0.3 on 2024-04-30 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='kind',
            field=models.IntegerField(choices=[(0, 'Savings'), (1, 'Broker'), (2, 'Card')], default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='AccountReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reference', models.CharField(max_length=4)),
                ('account_balance_cents', models.IntegerField(default=0)),
                ('month_balance_cents', models.IntegerField(default=0)),
                ('month_incomes_cents', models.IntegerField(default=0)),
                ('month_expenses_cents', models.IntegerField(default=0)),
                ('month_invested_cents', models.IntegerField(default=0)),
                ('month_dividends_cents', models.IntegerField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
            options={
                'unique_together': {('reference', 'account')},
            },
        ),
    ]
