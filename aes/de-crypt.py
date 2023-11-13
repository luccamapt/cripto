from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def encrypt_aes(plaintext, key):
  # Converte a chave para bytes
  key_bytes = key.encode('utf-8')

  # Verifica o tamanho da chave e preenche se necessário
  if len(key_bytes) not in [16, 24, 32]:
    # Use SHA-256 para estender a chave para 16 bytes
    key_bytes = hashlib.sha256(key_bytes).digest()

  # Converte o texto para bytes
  plaintext_bytes = plaintext.encode('utf-8')

  # Cria um objeto AES com modo ECB
  cipher = AES.new(key_bytes, AES.MODE_ECB)

  # Criptografa o texto com preenchimento PKCS7
  ciphertext = cipher.encrypt(pad(plaintext_bytes, AES.block_size))

  # Converte o resultado de volta para uma string hexadecimal
  ciphertext_hex = ciphertext.hex()
  return ciphertext_hex

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

  # Descriptografa o texto cifrado com preenchimento PKCS7
  decrypted_text_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)

  # Converte o resultado de volta para uma string
  decrypted_text = decrypted_text_bytes.decode('utf-8')
  return decrypted_text

while True:
  print("\nMenu:")
  print("1. Encriptar")
  print("2. Decriptar")
  print("3. Sair")

  choice = input("Escolha uma opção (1/2/3): ")

  if choice == '1':
    # Entrada da chave
    key = input("Digite a chave: ")
    # Entrada do texto que se deseja encriptar
    plaintext = input("Digite o texto que deseja encriptar: ")
    # Encripta o texto
    ciphertext_hex = encrypt_aes(plaintext, key)
    # Imprime o texto encriptado
    print('Texto Encriptado:', ciphertext_hex)

  elif choice == '2':
    # Entrada da chave
    key = input("Digite a chave: ")
    # Entrada do texto cifrado em hexadecimal
    ciphertext_hex = input("Digite o texto cifrado em hexadecimal: ")
    # Decripta o texto
    plaintext = decrypt_aes(ciphertext_hex, key)
    # Imprime o texto decriptado
    print('Texto Decriptado:', plaintext)

  elif choice == '3':
    print("Saindo do programa.")
    break

  else:
    print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
