from solana.constants import LAMPORTS_PER_SOL
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair
from solders.message import Message
from solders.system_program import TransferParams, transfer
from solders.transaction import Transaction

from utils.func import keypair_from_file


class SolanaAPI:
    """A class to interact with the Solana API.

    Attributes:
        url (str): The URL of the Solana API.
        address (str): The address of the account.
        client (AsyncClient): The client to interact with the Solana API
    """
    def __init__(self, url, keypair=None):
        """The constructor for the SolanaAPI class.

        Parameters:
            url (str): The URL of the Solana API.
            address (str): The address of the account.
        """
        self.url = url
        self.account = keypair or keypair_from_file('keypair.json')
        self.client = AsyncClient(self.url)


    async def get_balance(self) -> int:
        """Get the balance of the account.

        Returns:
            int: The balance of the account in SOL.
        """
        balance = await self.client.get_balance(self.account.pubkey())
        return balance.value / 10**9
    
    async def get_account_info(self) -> dict:
        """Get the account info of the account.

        Returns:
            dict: The account info of the account.
        """
        account_info = await self.client.get_account_info(self.account.pubkey())
        return account_info.value
    
    async def get_last_blockhash(self) -> str:
        """Get the last blockhash.

        Returns:
            str: The last blockhash.
        """
        blockhash = await self.client.get_latest_blockhash()
        return blockhash.value.blockhash

    async def transfer(self, amount: float, receiver: Keypair) -> str:
        """Transfer the amount to the specified address.

        Parameters:
            to (str): The address to transfer the amount.
            amount (int): The amount to transfer.
        """
        amount = int(amount * LAMPORTS_PER_SOL)
        sender = self.account
        ixns = [
            transfer(
                TransferParams(from_pubkey=sender.pubkey(), to_pubkey=receiver.pubkey(), lamports=amount)
            )
        ]

        message = Message(ixns, sender.pubkey())
        last_block = await self.get_last_blockhash()
        transaction = await self.client.send_transaction(Transaction([sender], message, last_block))
        return transaction.value
