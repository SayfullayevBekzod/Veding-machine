from ichimlik import Ichimlik
from tolov import Tolov
from column import Column

class VedingMachine:
    def __init__(self) -> None:
        self.beverage_list: list[Ichimlik] = []
        self.card_list: list[Tolov] = []
        self.column_list: list[Column] = [Column(i) for i in range(1, 5)]

    def get_column(self, name):
        for column in self.column_list:
            if column.ichimlik == name:
                return column
        return -1.0

    def sell(self, name, card_id):
        price_baverage = self.get_price(name)
        card = self.get_credit(card_id)
        if card >= price_baverage and card != -1.0:
            for card_in in self.card_list:
                if card_in.card_id == card_id:
                    card_in.rashod(price_baverage)
                    column_number = self.get_column(name)
                    column_number.kamaytirish()
                    return "changed credit card"
            return self.get_column(name)
        return -1.0


    def refill_column(self, id, beverage, cans):
        column = self.column_list[id - 1]
        column._ichimlik = beverage
        if column.number is not None:
            column.number += cans
        else:
            column.number = cans

    def available_cans(self, name):
        count = 0
        for column in self.column_list:
            if column.ichimlik == name:
                count += column.number
        return count

    def add_beverage(self, ichimlik: Ichimlik):
        if ichimlik not in self.beverage_list:
            self.beverage_list.append(ichimlik)
            return "appended"
        return "dublicated"

    def get_price(self, ichimlik_nomi):
        for ichimlik in self.beverage_list:
            if ichimlik.nomi == ichimlik_nomi:
                return ichimlik.narxi
        return -1.0

    def recharge_card(self, card_id, credit):
        for card in self.card_list:
            if card.card_id == card_id:
                card.recharge(credit)
                return "recharged"
        card = Tolov(card_id, credit)
        self.card_list.append(card)
        return "card appended"

    def get_credit(self, card_id):
        for card in self.card_list:
            if card.card_id == card_id:
                return card.credit
        return -1.0
        
