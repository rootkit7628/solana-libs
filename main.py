import asyncio
import os

from dotenv import load_dotenv

from services.solana import SolanaAPI

load_dotenv()
URL = os.getenv("URL")
ADDRESS = os.getenv("ADDRESS")


async def main():
    if URL and ADDRESS:
        api = SolanaAPI(URL, ADDRESS)
        balance = await api.get_balance()
        account_info = await api.get_account_info()

        print(f"Balance : {balance} SOL")
        print(f"Account Info : {account_info}")
    else:
        print("Please set the URL and ADDRESS .env file.")


if __name__ == "__main__":
    asyncio.run(main())
