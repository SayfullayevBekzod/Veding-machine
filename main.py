from ichimlik import Ichimlik
from machine import VedingMachine
from tolov import Tolov

machine = VedingMachine()

print(machine.get_credit(1425))
machine.recharge_card(1425, 25000)
machine.recharge_card(1425, 25000)
ichimlik = Ichimlik('fanta', 10000)
machine.add_beverage(ichimlik)
machine.refill_column(1, 'fanta', 5)
print(machine.sell('fanta', 1425))
print(machine.sell('fanta', 1425))
print(machine.get_credit(1425))
print(machine.available_cans('fanta'))

'''#machine.addBevarg(Ichimlik( "Coca Cola", 2))
#machine.addBevarg(Ichimlik( "Pepsi", 2))
#machine.addBevarg(Ichimlik( "Sprite", 2))
#machine.addBevarg(Ichimlik( "Fanta", 2))
#machine.addBevarg(Ichimlik( "Ayran", 1))
#machine.addBevarg(Ichimlik( "Soda", 1))
#machine.addBevarg(Ichimlik( "Su", 1))
#machine.addBevarg(Ichimlik( "Cappy", 3))
#machine.addBevarg(Ichimlik( "Pulpy", 3))
#machine.addBevarg(Ichimlik( "Narsharab", 4))
#machine.addBevarg(Ichimlik( "Meyvadar", 4))
#machine.addBevarg(Ichimlik( "Limonad", 2))
#machine.addBevarg(Ichimlik( "Qora Choy", 2))
#machine.addBevarg(Ichimlik( "Qora Qaymoq", 2))
#machine.addBevarg(Ichimlik( "Shokolad Suyu", 3))
#machine.addBevarg(Ichimlik( "Qora Cho'pon", 2))
#machine.addBevarg(Ichimlik( "Choy", 1))
#machine.addBevarg(Ichimlik( "Shokolad Sut", 3))
#machine.addBevarg(Ichimlik( "Sut", 2))
#machine.addBevarg(Ichimlik( "Doimiy", 1))
#for ichimlik in machine.ichimlik_list:
#    print(f"{ichimlik.nomi}: {machine.aviableCans(ichimlik.nomi)} ta")'''

