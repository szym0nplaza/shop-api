from modules.products.application.interfaces import IPaymentGateway
from modules.products.application.dto import PaymentDTO
from modules.products.domain.models import Product
from config.settings import settings
import stripe

stripe.api_key = settings.stripe_key


class PaymentGateway(IPaymentGateway):
    def create_payment(self, dto: PaymentDTO, product: Product, seller_stripe_id: str):
        token = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": str(dto.card_number),
                "exp_month": dto.exp_month,
                "exp_year": dto.exp_year,
                "cvc": dto.cvc
            }
        )

        self.intent = stripe.PaymentIntent.create(
            amount=int(product.price*100),
            currency=dto.currency,
            payment_method=token.id,
            customer=seller_stripe_id
        )

        

    def confirm_payment(self):
        payment_intent_id = self.intent.id

        stripe.PaymentIntent.confirm(
            payment_intent_id,
            payment_method=self.intent.payment_method,
        )
