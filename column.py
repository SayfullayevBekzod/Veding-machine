class Column:
    def __init__(self, id) -> None:
        self._id = id
        self._ichimlik = None
        self._number = None

    @property
    def id(self):
        return self._id
    
    @property
    def ichimlik(self):
        return self._ichimlik
    
    @ichimlik.setter
    def ichimlik(self, value):
        self._ichimlik = value

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, value):
        self._number = value

    @property
    def son(self):
        return self._son
    
    @son.setter
    def son(self, value):
        self._son = value
        
    def kamaytirish(self):
        self._number -= 1