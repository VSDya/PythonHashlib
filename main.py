import hashlib

# Пример данных для хеширования
data = b"Hello, World!"

# Вычисление хэша SHA-256
sha256 = hashlib.sha256(data).hexdigest()
print("SHA-256:", sha256)

# Вычисление хэша MD5
md5 = hashlib.md5(data).hexdigest()
print("MD5:", md5)

# Вычисление хэша SHA-1
sha1 = hashlib.sha1(data).hexdigest()
print("SHA-1:", sha1)

# Вычисление хэша SHA-512
sha512 = hashlib.sha512(data).hexdigest()
print("SHA-512:", sha512)

# Вычисление хэша RIPEMD-160
ripemd160 = hashlib.new("ripemd160", data).hexdigest()
print("RIPEMD-160:", ripemd160)

# import hashlib

# def calculate_hash(input_string, algorithm='sha256'):
#     hash_object = hashlib.new(algorithm)
#     hash_object.update(input_string.encode('utf-8'))
#     return hash_object.hexdigest()

# if __name__ == '__main__':
#     input_string = 'Пример строки для хэширования'
#     hash_value = calculate_hash(input_string, 'sha256')
#     print(f'SHA-256: {hash_value}')
    
#     hash_value_md5 = calculate_hash(input_string, 'md5')
#     print(f'MD5: {hash_value_md5}')
