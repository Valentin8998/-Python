from smartphone import Smartphone
catalog = [
    Smartphone('Apple', '17', '+79995558585'),
    Smartphone('Xiaomi', '17t', '+79008548547'),
    Smartphone('Redmi', 'Mi', '89784563223'),
    Smartphone('Oppo', 'z', '+78521236589'),
    Smartphone('Nokia', '3310', '+79854123658')
]

for smartphone in catalog:
    print(f'{smartphone.mark} - {smartphone.mod}.  {smartphone.num}')
