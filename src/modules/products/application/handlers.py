from .interfaces import IOrderRepository, IProductRepository
from .dto import ProductDTO, CreateProductDTO
from modules.products.domain.models import Product


class ProductHandler:
    def __init__(self, repo: IProductRepository) -> None:
        self._repo = repo

    def add_product(self, dto: CreateProductDTO):
        with self._repo:
            self._repo.add_product(dto)

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

