import pyaes
import secrets

def encrypt_file(file_path, key):
    chunk_size = 64 * 1024  # 64 KB chunks
    encrypter = pyaes.AESModeOfOperationCTR(key)

    with open(file_path, 'rb') as infile:
        plaintext = infile.read()
        ciphertext = encrypter.encrypt(plaintext)

    with open(file_path + ".encrypted", 'wb') as outfile:
        outfile.write(ciphertext)

if __name__ == "__main__":
    key = secrets.token_bytes(32)  # Gera uma chave de 32 bytes aleatória
    encrypt_file('mensagem.txt', key)
