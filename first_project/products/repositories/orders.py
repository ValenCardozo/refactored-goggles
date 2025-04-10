from products.models import Order

class OrderRepository:
    """
    Clase de repositorio que se encargara de conectarse con la db
    para manipular ordenes
    """

    @staticmethod
    def get_all() -> list[Order]:
        """
        Obtiene todos los objects (Order)
        """
        return Order.objects.all()