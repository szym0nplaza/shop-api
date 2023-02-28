from abc import ABC, abstractmethod


class IProductRepository(ABC):
    def __enter__(self):
        pass

    def __exit__(self, *__args) -> None:
        pass

    @abstractmethod
    def add_product(self, dto):
        raise NotImplementedError
    
    @abstractmethod
    def get_product(self, id: int):
        raise NotImplementedError
    
    @abstractmethod
    def get_products(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_seller_products(self, seller_id: int):
        raise NotImplementedError
    
    @abstractmethod
    def delete_product(self, id: int):
        raise NotImplementedError
    

class IOrderRepository(ABC):
    @abstractmethod
    def add_order(self, dto):
        raise NotImplementedError
    
    @abstractmethod
    def get_order(self, id: int):
        raise NotImplementedError
    
    @abstractmethod
    def get_orders(self, user_id: int):
        raise NotImplementedError
    
    @abstractmethod
    def delete_order(self, id: int):
        raise NotImplementedError


class IPaymentGateway(ABC):
    @abstractmethod
    def create_payment(self, dto, product, customer_name: str):
        raise NotImplementedError
    
    @abstractmethod
    def confirm_payment(self, seller_stripe_id: str):
        raise NotImplementedError