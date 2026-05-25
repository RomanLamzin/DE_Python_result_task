from collections import defaultdict

purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(purchases):
    result = 0
    for i in range(len(purchases)):
        result += purchases[i].get('price') * purchases[i].get('quantity')

    print(f"Общая выручка: {result}")


def items_by_category(purchases):
    result = {}
    for i in range(len(purchases)):
        result.setdefault(purchases[i].get('category'), []).append(purchases[i].get('item'))

    print(f'Товары по категориям: {result}')


def expensive_purchases(purchases, min_price: float):
    result = []
    for i in purchases:
        if min_price <= i.get('price'):
            result.append(i)
    print(f'Покупки дороже {min_price}: {result}')


def average_price_by_category(purchases):
    get_all_price = {}
    for i in range(len(purchases)):
        get_all_price.setdefault(purchases[i].get('category'), []).append(purchases[i].get('price'))

    res_avg = {}
    for i in get_all_price:
        res_avg[i] = sum(get_all_price.get(i)) / len(get_all_price.get(i))

    print(f'Средняя цена по категориям: {res_avg}')


def most_frequent_category(purchases):
    count_all_category = defaultdict(int)

    for item in purchases:
        count_all_category[item["category"]] += item["quantity"]

    result = max(count_all_category, key=count_all_category.get)

    print(f'Категория с наибольшим количеством проданных товаров: {result}')

total_revenue(purchases)
items_by_category(purchases)
expensive_purchases(purchases, 1)
average_price_by_category(purchases)
most_frequent_category(purchases)