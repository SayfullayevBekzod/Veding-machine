class Ichimlik:
    def __init__(self, nomi: str, narxi: int) -> None:
        self._nomi = nomi
        self._narxi =  narxi
    @property
    def nomi(self):
        return self._nomi
    @property
    def narxi(self):
        return self._narxi
    def __str__(self) -> str:
        return f"{self._nomi} --> {self._narxi}"
    def __eq__(self, __value: object) -> bool:
        return self.narxi == __value.narxi and self.nomi == __value.nomi