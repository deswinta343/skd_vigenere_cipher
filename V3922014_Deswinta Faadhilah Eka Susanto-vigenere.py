import numpy as np

def generate_vigenere_matrix(key):
    # Konversi kunci ke dalam bentuk angka berdasarkan tabel ASCII
    key_as_int = [ord(char) - 65 for char in key.upper()]

    # Buat matriks Vigenère berdasarkan kunci
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(key_as_int[(i * 3 + j) % len(key_as_int)])
        matrix.append(row)

    return np.array(matrix)

def vigenere_encrypt(message, key):
    matrix = generate_vigenere_matrix(key)

    # Ubah pesan ke dalam bentuk yang sesuai untuk enkripsi
    message = message.replace(" ", "").upper()

    # Buat matriks pesan yang akan dienkripsi
    message_matrix = []
    for i in range(0, len(message), 3):
        chunk = message[i:i+3]
        while len(chunk) < 3:
            chunk += 'X'  # Tambahkan 'X' jika panjangnya kurang dari 3
        chunk_int = [ord(char) - 65 for char in chunk]
        message_matrix.append(chunk_int)

    encrypted_message = ""
    for chunk in message_matrix:
        result = np.dot(matrix, chunk) % 26
        encrypted_message += ''.join([chr(char + 65) for char in result])

    return encrypted_message

# Kalimat yang ingin dienkripsi
plaintext = "Have fun studying cryptography"
key = "DESWINTAF"

# Enkripsi pesan dengan menggunakan metode Vigenère cipher
encrypted_text = vigenere_encrypt(plaintext, key)
print("Pesan Terenkripsi:", encrypted_text)
