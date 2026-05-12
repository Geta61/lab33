from src.providers.provider_a.provider_a_factory import ProviderAFactory
from src.providers.provider_a.provider_a_client import ProviderAClient


def test_provider_a_factory_creates_a_components():

    factory = ProviderAFactory()

    client = factory.create_client()

    assert isinstance(client, ProviderAClient)
