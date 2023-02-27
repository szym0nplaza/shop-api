from modules.products.application.interfaces import (
    IOrderRepository,
    IProductRepository,
    IPaymentGateway,
)


def id_generator():
    id = 1
    while True:
        yield id
        id += 1


class MockOrderRepo(IOrderRepository):
    pass


class MockProductRepo(IProductRepository):
    pass


class MockPaymentRepo(IPaymentGateway):
    pass
