from address import Address
from mailing import Mailing
address12 = Address('178', 'Москва', 'ул.мира', '14a', '3')
address21 = Address('234', 'Омск', 'ул.Ленина', '25', '46')
mailing = Mailing(
    to_address=address12, from_address=address21, cost=489, track="N528"
    )
print(f"Отправление {mailing.track} из {mailing.from_address}"
      f" в {mailing.to_address}. Стоимость {mailing.cost} рублей.")
