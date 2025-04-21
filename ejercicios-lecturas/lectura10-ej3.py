import hashlib

def calc_hash(filepath, algorithm='sha1'):
    h = hashlib.new(algorithm)
    with open(filepath, 'rb') as file:
        chunk = file.read(8192)
        while chunk:
            h.update(chunk)
            chunk = file.read(8192)
    return h.hexdigest()

path = 'Lectura 11-v1.md'
sha1 = calc_hash(path, 'sha1')
print(f'\nPara {path}\nSHA1: {sha1}')

path = 'Lectura 11-v2.md'
sha1 = calc_hash(path, 'sha1')
print(f'\nPara {path}\nSHA1: {sha1}')

path = 'Lectura 11-v2 copy.md'
sha1 = calc_hash(path, 'sha1')
print(f'\nPara {path}\nSHA1: {sha1}')