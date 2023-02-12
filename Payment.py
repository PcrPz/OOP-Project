class Payment:
    def __init__(self,payment_status,transaction_id,amount,card_info):
        self._payment_status = payment_status
        self._transaction_id = transaction_id
        self._amount = amount
        self._card_info = card_info