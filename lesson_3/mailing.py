from address_1 import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

to_address = Address("5555", "Volgograd", "Ulitsa Nepokorennykh", "4", "35")
from_address = Address("2222", "Moscow", "Ulitsa Pervogo Maya", "19", "333")

mailing = Mailing(to_address, from_address, 100, "RU123456789") 