import phonenumbers

number = phonenumbers.parse("+2348168622857", None)
print(phonenumbers.is_valid_number(number))
