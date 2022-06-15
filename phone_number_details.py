import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

phone_number = input("[+] enter phone nuber to check (including ccountry code): ")
num = phonenumbers.parse(phone_number)

print(num)
print(f"is valid number: {phonenumbers.is_valid_number(num)}")
print(f"region: {geocoder.description_for_number(num, 'en')}")
print(f"service provider: {carrier.name_for_number(num, 'en')}")
print(f"timezone: {timezone.time_zones_for_number(num)}")