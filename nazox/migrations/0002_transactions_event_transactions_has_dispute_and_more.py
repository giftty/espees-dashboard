# Generated by Django 4.2.4 on 2024-02-14 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nazox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='event',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='transactions',
            name='has_dispute',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transactions',
            name='account_No',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='card_country',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='channel',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='channel_Type',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='country',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='currency',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='fee',
            field=models.CharField(default=0, max_length=400),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='gateway_Response_Code',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='gateway_response_Message',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='is_International',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='is_Nigerian_Card',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='linking_reference',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='mode',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='prev_Linking_Reference',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='reason',
            field=models.CharField(default=' ', max_length=500),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='refund_Amount',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='settlement_Amount',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='status',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transType',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_Fee',
            field=models.CharField(default=0, max_length=400),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_description',
            field=models.CharField(default=' ', max_length=400),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_reference',
            field=models.CharField(default=' ', max_length=400),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_time',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transfer_amount',
            field=models.CharField(default=0, max_length=400),
        ),
    ]
