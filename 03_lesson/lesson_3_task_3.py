from address import Address
from mailing import Mailing


to_address = Address("117042", "Москва", "Венёвская", "5", "2")
from_address = Address("105037", "Москва", "Измайловская", "20", "40")


mailing = Mailing(to_address, from_address, 123, "SG141115188")


print(f"Отправление {mailing.track} из {mailing.to_address.index}, "
      f"{mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.flat} в  "
      f"{mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - "
      f"{mailing.from_address.flat}. Стоимость {mailing.cost} рублей.")
