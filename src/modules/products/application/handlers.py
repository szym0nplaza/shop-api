from .interfaces import IOrderRepository, IProductRepository
from .dto import ProductDTO, CreateProductDTO, OrderDTO, CreateOrderDTO
from modules.products.domain.models import Product, Order


class ProductHandler:
    def __init__(self, repo: IProductRepository) -> None:
        self._repo = repo

    def add_product(self, dto: CreateProductDTO):
        with self._repo:
            instance = Product(**dto.__dict__)
            self._repo.add_product(instance)

    def get_product(self, id: int):
        with self._repo:
            record = self._repo.get_product(id)
            result = ProductDTO(**record.__dict__)
            return result
        
    def get_products(self):
        with self._repo:
            qs = self._repo.get_products()
            result = [ProductDTO(**record.__dict__) for record in qs]
            return result
        
    def get_seller_products(self, seller_id: int):
        with self._repo:
            qs = self._repo.get_seller_products(seller_id)
            result = [ProductDTO(**record.__dict__) for record in qs]
            return result
        
    def udpate_product(self, dto: ProductDTO):
        with self._repo:
            product: Product = self._repo.get_product(dto.id)
            product.update_data(dto)

    def delete_product(self, id: int):
        with self._repo:
            self._repo.delete_product(id)


class OrderHandler:
    def __init__(self, repo: IOrderRepository) -> None:
        self._repo = repo

    def add_order(self, dto: CreateOrderDTO):
        with self._repo:
            instance = Order(**dto.__dict__)
            self._repo.add_order(instance)

    def get_order(self, id: int):
        with self._repo:
            record = self._repo.get_order(id)
            result = OrderDTO(**record.__dict__)
            return result
        
    def get_orders(self, user_id: int):
        with self._repo:
            qs = self._repo.get_orders(user_id)
            result = [OrderDTO(**record.__dict__) for record in qs]
            return result
        
    def udpate_order(self, dto: OrderDTO):
        with self._repo:
            order: Order = self._repo.get_order(dto.id)
            order.update_data(dto)

    def delete_order(self, id: int):
        with self._repo:
            order: Order = self._repo.get_order(id)
            order.check_possibility_to_delete()
            self._repo.delete_order(id)

