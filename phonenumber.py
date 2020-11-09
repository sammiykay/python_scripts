import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
num = input("Enter phone number with country code: ")

numbers = phonenumbers.parse(num)

print(geocoder.description_for_number(numbers, 'en'))
print(carrier.name_of_number(numbers, 'en'))