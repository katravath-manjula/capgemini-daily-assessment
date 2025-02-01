initial_stock = {"apple": 50,"banana": 100,"orange": 75}

sold_item = {"apple": 10, "banana": 20, "orange": 15}

for i in initial_stock:
    cureent_stock=({i:initial_stock[i]-sold_item[i]})
    print(cureent_stock)