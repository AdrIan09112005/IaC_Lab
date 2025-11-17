# Importación Cipher, algorithms, modes, default_backend y urandom
# From -> Para importar clases y funciones específicas de un módulo
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend # Importar el backend por defecto
from os import urandom

# Trabajamos con el algoritmo AES en modo CBC
def generar_clave_y_iv():
    "Generar una clave AES de 256 bits y un IV de 128 bits."
    # key significa 'clave', usado para encriptar y desencriptar
    key = urandom(32)  # 256 bits

    # iv significa 'initialization vector'
    iv = urandom(16)   # 128 bits
    return key, iv

# Función para encriptar texto plano 
def encriptar(texto_plano, key, iv):
    "Encriptar texto plano usando AES en modo CBC."
    # Objeto Cipher para encriptar (Encriptador)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Crear un encriptador
    encryptor = cipher.encryptor()

    # Padding para que el texto tenga una longitud múltiplo de 16 bytes
    # Esto es necesario para algunos modos de cifrado como CBC
    texto_plano_bytes = texto_plano.encode('utf-8') # Convertir el texto plano a bytes 

    # Calcular la longitud del padding necesario
    padding_length = 16 - (len(texto_plano_bytes) % 16) 

    # Calcular el padding para que el texto sea múltiplo de 16 bytes
    pading = bytes([padding_length] * padding_length)

    texto_a_cifrar = texto_plano_bytes + pading # Asegurar que el texto es múltiplo de 16 bytes
    texto_cifrado = encryptor.update(texto_a_cifrar) + encryptor.finalize() # Encriptar el texto cifrado
    return texto_cifrado

def desencriptar(texto_cifrado, key, iv):
    "Desencriptar texto cifrado usando AES en modo CBC."
    # Objeto Cipher para desencriptar (Desencriptador)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Crear un desencriptador
    decryptor = cipher.decryptor()

    # Desencriptar el texto cifrado
    texto_desencriptado_con_padding = decryptor.update(texto_cifrado) + decryptor.finalize()

    # Remover el padding
    padding_length = texto_desencriptado_con_padding[-1]  # Último byte indica la longitud del padding
    texto_desencriptado = texto_desencriptado_con_padding[:-padding_length]  # Remover el padding - [:-padding_length] quita los 
                                                                             # bytes de padding del final

    return texto_desencriptado.decode('utf-8')  # Convertir bytes a string    

# --- USO ---
# 1. Generar clave e IV (guardarlos para un uso futuro)
key, iv = generar_clave_y_iv()

# 2. Texto a encriptar (original)
texto_original = "Alan Adrian Estrada Alfaro"

# 3. encriptar el mensaje
texto_encriptado = encriptar(texto_original, key, iv)
print(f"Texto encriptado (bytes): {texto_encriptado}")

# 4. Desencriptar el mensaje
texto_desencriptado = desencriptar(texto_encriptado, key, iv)
print(f"Texto desencriptado: {texto_desencriptado}")