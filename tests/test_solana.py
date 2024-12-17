

from unittest import IsolatedAsyncioTestCase as TestCase

from solders.pubkey import Pubkey

from services.solana import SolanaAPI

URL = "https://api.devnet.solana.com"
ADDRESS = "2QGv7CNXJFYRUnkei6yZ88ygzE3peLTJB8c7kLXsuvzR"


class TestSolanaAPI(TestCase):
    async def test_init(self):
        solana = SolanaAPI(URL, ADDRESS)
        self.assertEqual(solana.url, URL    )
        self.assertEqual(solana.address, Pubkey.from_string(ADDRESS))
        self.assertIsNotNone(solana.client)
        self.assertTrue(await solana.client.is_connected())

    async def test_init_invalid_address(self):    
        address = "invalid"
        with self.assertRaises(ValueError):
            SolanaAPI(URL, address)

    async def test_get_balance(self):
        solana = SolanaAPI(URL, ADDRESS)
        balance = await solana.get_balance()
        self.assertIsNotNone(balance)
