products = "yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
product_list = products.split()
frequency_dict = {}
for product in product_list:
    frequency_dict[product] = frequency_dict.get(product, 0) + 1

print(frequency_dict)