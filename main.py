import asyncio
import os
from datetime import datetime

from dotenv import load_dotenv

from services.solana import SolanaAPI
from utils.func import generate_keypair

load_dotenv()
URL = os.getenv("URL")


async def main():
    if URL:
        api = SolanaAPI(URL)
        account_info = await api.get_account_info()
        print(f"Account Info : {account_info}")

        # Atcual balance
        balance = await api.get_balance()        
        print(f"Balance at {datetime.now()}: {balance} SOL\n")

        # Transfer 0.1 SOL to the second address
        receiver = generate_keypair()
        print(f"Transfering 0.2 SOL to the second to {receiver.pubkey()}")
        tranfer = await api.transfer(0.2, receiver)
        print(f"Transfer : {tranfer}")
    else:
        print("Please set the URL and ADDRESS .env file.")


if __name__ == "__main__":
    asyncio.run(main())
