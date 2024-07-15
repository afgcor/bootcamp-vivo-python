from store.usecases.product import product_usecase
from store.usecases.product import ProductOut

async def test_usecases_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Caderno Paperblanks Azure Midi"