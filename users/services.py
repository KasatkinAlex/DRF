import stripe
from config.settings import STRIPE_API_KEY


stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    """Создаем stripe продукт"""

    title_product = f'{instance.course_paid}' if instance.course_paid else f'{instance.lesson_paid}'
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get('id')


def create_stripe_price(stripe_product_id, amount):
    """Создаём stripe цену"""
    return stripe.Price.create(
        currency='rub',
        unit_amount=int(amount * 100),
        product=stripe_product_id,)


def create_stripe_session(price):
    """Создаём stripe сессию"""
    session = stripe.checkout.Session.create(success_url="http://127.0.0.1:8000/user/payment/",
                                             line_items=[{"price": price.get("id"), "quantity": 1}],
                                             mode="payment")
    return session.get("id"), session.get("url")
