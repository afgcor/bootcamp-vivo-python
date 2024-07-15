from uuid import UUID
from pydantic import ValidationError
import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data

def test_schemas_validated():
    product = ProductIn.model_validate(product_data)

    assert product.name == "Caderno Paperblanks Azure Midi"
    assert isinstance(product.id, UUID)

def test_schemas_return_raise():
    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(product_data)

    assert err.value.errors()[0] ==  {
        "type": "missing", "loc": ("status",), "msg": "Field required", "input": {"name": "Caderno Paperblanks Azure Midi", "quantity": 2, "price": 180.0}, "url": "https://errors.pydantic.dev/2.5/v/missing",}