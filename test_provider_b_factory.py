from src.providers.provider_b.provider_b_factory import ProviderBFactory
from src.providers.provider_b.provider_b_client import ProviderBClient


def test_provider_b_factory_creates_b_components():

    factory = ProviderBFactory()

    client = factory.create_client()

    assert isinstance(client, ProviderBClient)
