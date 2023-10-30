from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

def decrypt_aes(ciphertext_hex, key):
  # Converte a chave para bytes
  key_bytes = key.encode('utf-8')

  # Verifica o tamanho da chave e preenche se necessário
  if len(key_bytes) not in [16, 24, 32]:
    # Use SHA-256 para estender a chave para 16 bytes
    key_bytes = hashlib.sha256(key_bytes).digest()

  # Converte o texto cifrado em hexadecimal de volta para bytes
  ciphertext = bytes.fromhex(ciphertext_hex)

  # Cria um objeto AES com modo ECB
  cipher = AES.new(key_bytes, AES.MODE_ECB)

  # Descriptografa o texto cifrado
  decrypted_text_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)

  # Converte o resultado de volta para uma string
  decrypted_text = decrypted_text_bytes.decode('utf-8')
  return decrypted_text

# Entrada da chave
key = input("Digite a chave: ")

# Entrada do texto cifrado em hexadecimal
ciphertext_hex = input("Digite o texto cifrado em hexadecimal: ")

# Decifra o texto
plaintext = decrypt_aes(ciphertext_hex, key)

# Imprime o texto decifrado
print('Texto Decifrado:', plaintext)
