from num2words import num2words

narx = float(input("narx: "))
narx2 = float(input("narx: "))
narx3 = float(input("narx: "))

umumiy = round(narx + narx2 + narx3, 1)

soz_en = num2words(umumiy, to='currency', currency='USD')
soz_ru = num2words(umumiy, lang='ru', to='currency', currency='USD')

print(umumiy, soz_en, soz_ru)
