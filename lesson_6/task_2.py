stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def calc_total_price(stock_dct: dict, prices_dct: dict) -> float:
    total_price = 0.0
    for k in stock_dct:
        total_price = total_price + stock_dct[k] * prices_dct[k]
    return total_price


customer_total_price = calc_total_price(stock, prices)
print(customer_total_price)