def init_rc4(key):
  # Converte a chave em uma lista de números inteiros representando os bytes
  key = [ord(char) for char in key]
  S = list(range(256))
  j = 0
  # Inicializa o estado S permutando-o com base na chave
  for i in range(256):
    j = (j + S[i] + key[i % len(key)]) % 256
    S[i], S[j] = S[j], S[i]
  return S

def generate_keystream(S, text_length):
  i, j = 0, 0
  keystream = []
  for _ in range(text_length):
    i = (i + 1) % 256
    j = (j + S[i]) % 256
    S[i], S[j] = S[j], S[i]
    k = S[(S[i] + S[j]) % 256]
    keystream.append(k)
  return keystream

def decrypt(text_hex, key):
  S = init_rc4(key)
  # Converte o texto cifrado em hexadecimal de volta para bytes
  text_bytes = bytes.fromhex(text_hex)
  # Gera o keystream
  keystream = generate_keystream(S, len(text_bytes))
  # Realiza a operação XOR entre o texto cifrado e o keystream
  decrypted_bytes = bytes([x ^ y for x, y in zip(text_bytes, keystream)])
  # Converte o resultado de volta para uma string
  decrypted_text = decrypted_bytes.decode('utf-8')
  return decrypted_text

# Entrada do usuário: texto cifrado em hexadecimal e chave separados por espaço
user_input = input("Digite o texto cifrado em hexadecimal e a chave separados por espaço: ")
ciphertext_hex, key = user_input.split()

# Decifra o texto
plaintext = decrypt(ciphertext_hex, key)

# Imprime o texto decifrado
print('Texto Decifrado:', plaintext)
