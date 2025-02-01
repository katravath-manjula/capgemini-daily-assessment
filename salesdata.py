sales_data = [
    {"region": "North", "sales": 15000},
    {"region": "South", "sales": 8000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000},
    {"region": "West", "sales": 7000},
    {"region": "East", "sales": 5000},
    {"region": "South", "sales": 12000}
]
total_sales={}
for em in sales_data:
    region=em["region"]
    sales=em["sales"]
    total_sales[region]=total_sales.get(region,0)+sales

for region,total in total_sales.items():    
       print(f'{region} : {total}')