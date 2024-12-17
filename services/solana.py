from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey


class SolanaAPI:
    """A class to interact with the Solana API.

    Attributes:
        url (str): The URL of the Solana API.
        address (str): The address of the account.
        client (AsyncClient): The client to interact with the Solana API
    """
    def __init__(self, url, address):
        """The constructor for the SolanaAPI class.

        Parameters:
            url (str): The URL of the Solana API.
            address (str): The address of the account.
        """
        self.url = url
        self.address = Pubkey.from_string(address)
        self.client = AsyncClient(self.url)


    async def get_balance(self):
        """Get the balance of the account.

        Returns:
            int: The balance of the account in SOL.
        """
        balance = await self.client.get_balance(self.address)
        return balance.value / 10**9
    
    async def get_account_info(self):
        """Get the account info of the account.

        Returns:
            dict: The account info of the account.
        """
        account_info = await self.client.get_account_info(self.address)
        return account_info.value
