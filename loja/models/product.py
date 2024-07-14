from loja.models.base import CreateBaseModel
from loja.schema.product import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    ...
