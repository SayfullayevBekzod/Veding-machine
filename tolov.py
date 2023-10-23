class Tolov:
    def __init__(self, card_id, credit):
        self._card_id = card_id
        self._credit = credit

    @property
    def card_id(self):
        return self._card_id

    def recharge(self, value):
        self._credit += value

    def rashod(self, debit):
        self._credit -= debit
    
    def recharge(self, value):
        self._credit += value

    @property
    def credit(self):
        return self._credit
    
    def __str__(self) -> str:
        return str(self._card_id) + " ---> " + str(self._credit)