from num2words import num2words

amount = int(input("Pul miqdorini kiriting ($): "))

fifty = amount // 50
amount %= 50

ten = amount // 10
amount %= 10

five = amount // 5
amount %= 5

one = amount 
print(f"$50 kupyuradan: {fifty} ta")
print(f"$10 kupyuradan: {ten} ta")
print(f"$5 kupyuradan: {five} ta")
print(f"$1 kupyuradan: {one} ta")


total = fifty*50 + ten*10 + five*5 + one
words_en = num2words(total, lang='en')
words_ru = num2words(total, lang='ru')

print(f"Umumiy summa: ${total} ({words_en}, {words_ru})")
