# DE_Python_result_task

Cкрипт на Python, который выполняет анализ данных по покупкам в магазине. 
У вас есть набор данных о покупках, и вам нужно провести различные аналитические операции, чтобы предоставить отчет.

Есть список покупок.
```Python
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
```              
## Реализованно несколько функций для анализа данных:

total_revenue(purchases): Рассчитайте и верните общую выручку (цена * количество для всех записей).

items_by_category(purchases): Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.

expensive_purchases(purchases, min_price): Выведите все покупки, где цена товара больше или равна min_price.

average_price_by_category(purchases): Рассчитайте среднюю цену товаров по каждой категории.

most_frequent_category(purchases): Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).


## Формат вывода должен соответствовать шаблону вида
```bash
Общая выручка: 23.5
Товары по категориям: {'fruit': ['apple', 'banana'], 'dairy': ['milk'], 'bakery': ['bread']}
Покупки дороже 1.0: [{'item': 'apple', 'category': 'fruit', 'price': 1.2, 'quantity': 10}, {'item': 'milk', 'category': 'dairy', 'price': 1.5, 'quantity': 2}, {'item': 'bread', 'category': 'bakery', 'price': 2.0, 'quantity': 3}]
Средняя цена по категориям: {'fruit': 0.85, 'dairy': 1.5, 'bakery': 2.0}
Категория с наибольшим количеством проданных товаров: fruit
```
