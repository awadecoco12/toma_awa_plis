import pywhatkit

numbers = int(input("How many numbers will you text to?: "))

for _ in range(numbers):
    phone_number = input("Enter phone number: ")
    text = input("What do you want to text that phone number?: ")
    pywhatkit.sendwhatmsg(phone_number, text, 16, 52)