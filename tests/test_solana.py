from unittest import IsolatedAsyncioTestCase as TestCase
from solders.keypair import Keypair
from services.solana import SolanaAPI


URL = "https://api.devnet.solana.com"
ACCOUNT = Keypair() # Generate a random keypair


class TestSolanaAPI(TestCase):
    async def test_init(self):
        solana = SolanaAPI(URL, ACCOUNT)
        self.assertEqual(solana.url, URL)
        self.assertIsInstance(solana.account, Keypair)
        self.assertIsNotNone(solana.client)
        self.assertTrue(await solana.client.is_connected())

    async def test_get_balance(self):
        solana = SolanaAPI(URL, ACCOUNT)
        balance = await solana.get_balance()
        self.assertIsNotNone(balance)
    
    async def test_get_last_blockhash(self):
        solana = SolanaAPI(URL, ACCOUNT)
        blockhash = await solana.get_last_blockhash()
        self.assertIsNotNone(blockhash)