from modules.products.application.interfaces import IProductRepository
from modules.products.domain.models import Product, Order
from sqlalchemy.orm import Session
from config.settings import DBSession
from typing import List


class ProductRepository(IProductRepository):
    def __init__(self, session_class=DBSession()) -> None:
        self._session_class = session_class

    def __enter__(self) -> None:
        self._session: Session = self._session_class.get_session()

    def __exit__(self, *__args):
        try:
            self._session.commit()
        except:
            self._session.rollback()
        finally:
            self._session.close()

    def add_product(self, product: Product) -> None:
        return self._session.add(product)
    
    def get_product(self, id: int) -> Product:
        result = self._session.query(Product).filter_by(id=id).first()
        return result
    
    def get_products(self) -> List[Product]:
        result = self._session.query(Product).all()
        return result

    def get_seller_products(self, seller_id: int) -> Product:
        result = self._session.query(Product).filter_by(seller_id=seller_id).all()
        return result
    
    def delete_product(self, id: int):
        self._session.query(Product).filter_by(id=id).delete()