from num2words import num2words


monday = float(input("Miqdorni kiriting:"))
tuesday = float(input("Miqdorni kiriting:"))
wednesday = float(input("Miqdorni kiriting:"))
thursday = float(input("Miqdorni kiriting:"))
friday = float(input("Miqdorni kiriting:"))
saturday = float(input("Miqdorni kiriting:"))
sunday = float(input("Miqdorni kiriting:"))


price = (monday + tuesday + wednesday + thursday + friday + saturday + sunday)/7
result1_en = num2words(price, lang='en', to='currency', currency='USD')
result2_ru =  num2words(price, lang='ru', to='currency', currency='USD')

print(price)
print(result1_en)
print(result2_ru)