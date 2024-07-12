from address_1 import Address
from mailing import Mailing

to_address = Address("5555", "Volgograd", "Ulitsa Nepokorennykh", "4", "35")
from_address = Address("2222", "Moscow", "Ulitsa Pervogo Maya", "19", "333")
mailing = Mailing(to_address, from_address, 100, "RU123456789")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.") 