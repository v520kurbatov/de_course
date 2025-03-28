import json

with open(r'purchases.json', 'r', encoding='utf-8') as data:
    purchases = json.load(data)


def total_revenue(data: list[dict]) -> float:
    '''Возвращает общую выручку'''
    return sum(purchase['price'] * purchase['quantity'] for purchase in data)

def items_by_category(data: list[dict]) -> dict[str, list]:
    '''Возвращает словарь категорий и соответствующих им уникальных товаров'''
    res = {}
    for purchase in data:
        category = purchase['category']
        res.setdefault(category, [])
        if purchase['item'] not in res[category]:
            res[category].append(purchase['item'])
    
    return res

def expensive_purchases(data: list[dict], min_price: int | float) -> None:
    '''Выводит все покупки с ценой товара больше или равной min_price'''
    res = [purchase for purchase in data if purchase['price'] >= min_price]
    print(f'Покупки дороже {min_price}: {res}')

def average_price_by_category(data: list[dict]) -> dict[str, float]:
    '''Возвращает среднюю цену товаров по каждой категории'''
    res = {}
    for purchase in data:
        res.setdefault(purchase['category'], []).append(purchase['price'])

    for category in res:
        prices = res[category]
        res[category] = sum(prices) / len(prices)

    return res

def most_frequent_category(data: list[dict]) -> str:
    '''Возвращает категорию с наибольшим числом проданных товаров'''
    res = {}
    for purchase in data:
        category = purchase['category']
        res[category] = res.get(category, 0) + purchase['quantity']

    return max(res, key=res.get)

def get_report(data: list[dict]) -> None:
    '''Выводит отчет'''
    print(f'Общая выручка: {total_revenue(data)}')
    print(f'Товары по категориям: {items_by_category(data)}')
    expensive_purchases(data, 1.0)
    print(f'Средняя цена по категориям: {average_price_by_category(data)}')
    print(f'Категория с наибольшим количеством проданных товаров: {most_frequent_category(data)}')


get_report(purchases)