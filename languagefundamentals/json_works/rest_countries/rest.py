from json import load
f=open("C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\json_works\\rest_countries\\data.json",encoding="utf-8")
data=load(f)
print(len(data))

all_country_names=[c.get("name") for c in data]
print(all_country_names)

independent_country_names=[c.get("name") for c in data if c.get("independent")==True]
print(independent_country_names)
print(len(independent_country_names))

# print all regions
all_regions={c.get("region") for c in data}
print(all_regions)

# asian country names
asian_country_names=[c.get("name") for c in data if c.get("region")=="Asia" ]
print(asian_country_names)

# capital of Ukraine
capital_of_ukraine=[c.get("capital") for c in data  if c.get("name")=="Ukraine"]
print(capital_of_ukraine)

# print country name and captials
countries_and_capitals=[(c.get("name"),c.get("capital"))for c in data]
print(countries_and_capitals)

# print all country names and currencies
for c in data:
    if "currencies" in c:
        currency_data=c.get("currencies")[0]
        print(currency_data.get("name"),",",c.get("name"))

# print borders of india
india_borders=[c.get("borders") for c in data if c.get("name")=="India"][0]
print(india_borders)
india_border_names=[c.get("name") for c in data if c.get("alpha3Code") in india_borders]
print(india_border_names)

# print countries who have border names greater than 4

for c in data:
    if "borders" in c and len(c.get("borders"))>4:
        print(c.get("name"))