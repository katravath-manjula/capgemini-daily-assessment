inr_to_usd = 0.012
inr_to_eur = 0.011
PricesList_inr = [3000, 56000, 45000, 2300]

m = [inr_to_usd * i for i in PricesList_inr]
n = [inr_to_eur * i for i in PricesList_inr]

print(m)
print(n)