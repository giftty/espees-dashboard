
from django.db import models

class Transactions(models.Model) :
    id = models.AutoField(primary_key=True)
    transaction_time = models.CharField(max_length=200,default = " ")
    transaction_reference = models.CharField(max_length = 400,default = " ")
    transaction_description = models.CharField(max_length = 400,default = " ")
    linking_reference = models.CharField(max_length = 200,default = " ")
    amount =  models.CharField(max_length = 200,default = 0)
    currency =  models.CharField(max_length = 100,default = " ")
    country =  models.CharField(max_length = 50,default = " ")
    card_country =  models.CharField(max_length = 200,default = " ")
    is_Nigerian_Card =  models.CharField(max_length = 200,default = " ")
    prev_Linking_Reference =  models.CharField(max_length = 200,default = " ")
    transfer_amount =  models.CharField(max_length = 400,default = 0)
    transaction_Fee =  models.CharField(max_length = 400,default = 0)
    fee =  models.CharField(max_length = 400,default = 0)
    status =  models.CharField(max_length = 100,default = " ")
    reason =  models.CharField(max_length = 500,default = " ")
    account_No =  models.CharField(max_length = 100,default = " ")
    channel =  models.CharField(max_length = 100,default = " ")
    channel_Type =  models.CharField(max_length = 100,default = " ")
    is_International  =  models.CharField(max_length = 100,default = " ")
    mode  =  models.CharField(max_length = 100,default = " ")
    transType  =  models.CharField(max_length = 100,default = " ")
    settlement_Amount  =  models.CharField(max_length = 100,default = 0)
    refund_Amount  =  models.CharField(max_length = 100,default = 0)
    gateway_Response_Code  =  models.CharField(max_length = 200,default = " ")
    gateway_response_Message  =  models.CharField(max_length = 400,default = " ")
    has_dispute =  models.CharField(max_length = 50)
    event =  models.CharField(max_length = 200,default = " ")

