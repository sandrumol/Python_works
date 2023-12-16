from json import load
f=open("C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\json_works\\products\\items.json","r",encoding="utf-8")
data=load(f)

# print total number of products

# print(len(data))


# print category of product

product_category={product.get("category") for product in data}
# print(product_category)


# print count of electronics product

electronics_product=[product for product in data if product.get("category")=="electronics"]
# print(len(electronics_product))


# print count of jewellery product

jewelery_product=[product for product in data if product.get("category")=="jewelery"]
print(len(jewelery_product))


# print name of costly product

products_price=[product.get("price") for product in data ]
print(products_price)
max_price=max(products_price)
max_product=[product.get("title") for product in data if max_price==product.get("price")]
print(max_product)
