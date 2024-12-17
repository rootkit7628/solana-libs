import json

from solders.keypair import Keypair


def keypair_from_file(file: str) -> Keypair:
    with open(file, "r") as file:
        secretkey = json.load(file)
        return Keypair.from_bytes(secretkey)


def generate_keypair():
    return Keypair()
