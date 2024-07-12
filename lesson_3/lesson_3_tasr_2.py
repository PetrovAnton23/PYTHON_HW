from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Samsung", "Galaxy S21", "+790145689")
phone2 = Smartphone("Xiaomi", "Mi 5", "+7931543490")
phone3 = Smartphone("TECHNO", "TECHNO SPARK 9 pro", "+7954267890")
phone4 = Smartphone("Infinix", "Infinix Smart 8 Pro", "+7911456525")
phone5 = Smartphone("Apple", "iPhone 13 Pro Max", "+7934567890")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5) 

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")