from num2words import num2words
bir_kWh = 0.45

oy_boshi = float(input("Oy boshidagi ko‘rsatkich: "))
oy_oxiri = float(input("Oy oxiridagi ko‘rsatkich: "))

narx = oy_oxiri - oy_boshi

payment = round(narx * bir_kWh, 2)

payment_words_en = num2words(payment, lang='en', to='currency')
payment_words_ru = num2words(payment, lang='ru', to='currency')

print(f"To‘lov: ${payment} ({payment_words_en}, {payment_words_ru})")
