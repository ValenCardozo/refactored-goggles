from products.models import Order
from products.repositories.orders import OrderRepository

class OrderService:
    """
    Se puede utilizar con el init, y necesitan pasar siempre self
    
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_all(self) -> list[Product]:
        return self.product_repository.get_all()
    """
    
    @staticmethod
    def get_all() -> list[Order]:
        return OrderRepository.get_all() 
