from solders.keypair import Keypair
import base58

private_key_base58 = 'ENTER YOUR PRIVATE KEY'

# Dekode kunci privat dari base58 ke bytes
private_key_bytes = base58.b58decode(private_key_base58)

# Buat objek Keypair dari kunci privat
keypair = Keypair.from_bytes(private_key_bytes)

# Dapatkan alamat dompet
wallet_address = keypair.pubkey()

print(f"Wallet Address : {wallet_address}")
