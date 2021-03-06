from numpy import ceil


def shop_price_edit(goods: dict) -> dict:
    """Расчет стоимости товара с учетом 15% прибыли"""
    return {name: int(ceil((price + (price * 0.15)) / 5) * 5) for name, price in goods.items()}
