from num2words import num2words

first_bill = float(3.00)
way1km = float(1.20)
way = float(input("Masofa:"))

price = (way * way1km)+first_bill

taxi_narxi_en = num2words(
    price, 
    lang='en', 
    to='currency', 
    currency='USD'
    )

taxi_narxi_ru = num2words(
    price, 
    lang='ru', 
    to='currency', 
    currency='USD')


print(price, taxi_narxi_en, taxi_narxi_ru)
