import os
import base64

# Gera uma chave aleatória de 256 bits
key = os.urandom(32)

# Converte a chave em uma string de base64
encoded_key = base64.b64encode(key).decode('utf-8')

print(encoded_key)