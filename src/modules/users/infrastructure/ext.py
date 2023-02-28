from modules.users.application.intefraces import IPaymentGateway
from modules.users.domain.models import User
from config.settings import settings
import stripe


class PaymentGateway(IPaymentGateway):
    def create_seller_acc(self, user: User):
        payment = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": "4242424242424242",
                "exp_month": 12,
                "exp_year": 2032,
                "cvc": "314",
            },
        )
        customer = stripe.Customer.create(
            api_key=settings.stripe_key,
            email=user.email,
            description=f"Seller acc - {user.get_full_name()}",
            name=user.get_full_name(),
            
        )
        stripe.PaymentMethod.attach(payment, customer=customer.stripe_id)
        user.stripe_id = customer.stripe_id
        return user
