from json import load
f=open("C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\json_works\\currency_conversion\\data.json",encoding="utf-8")
data=load(f)

# convert an amount from USD TO INR

source_currency_code=input("Enter source currency code:") #USD
target_currency_code=input("Enter destination currency code:") #INR

amount=int(input("Enter amount:"))

conversion_rates=data.get("conversion_rates")
source_currency_rate=conversion_rates.get(source_currency_code)
destination_currency_rate=conversion_rates.get(target_currency_code)

# print(conversion_rates)
# print(source_currency_rate)
# print(destination_currency_rate)

res=(amount/source_currency_rate)*destination_currency_rate
print(res)

