import pyaes
import secrets

def decrypt_file(encrypted_file_path, key):
    encrypter = pyaes.AESModeOfOperationCTR(key)

    with open(encrypted_file_path, 'rb') as infile:
        ciphertext = infile.read()
        decrypted_text = encrypter.decrypt(ciphertext)

    decrypted_file_path = encrypted_file_path.replace('.encrypted', '_decrypted.txt')

    with open(decrypted_file_path, 'wb') as outfile:
        outfile.write(decrypted_text)

if __name__ == "__main__":
    key = secrets.token_bytes(32)  # Gera uma chave de 32 bytes aleatória
    decrypt_file('mensagem.txt.encrypted', key)
