import hashlib
import bcrypt

name = "Ahmad Karim"

md5_hash = hashlib.new('md5',name.encode()).hexdigest()
print("MD5",md5_hash)

SHA1_hash = hashlib.new('sha1',name.encode()).hexdigest()
print("SHA-1",SHA1_hash)

SHA2_hash = hashlib.new('sha256',name.encode()).hexdigest()
print("SHA-256",SHA2_hash)

SHA512_hash = hashlib.new('sha512',name.encode()).hexdigest()
print("SHA_512",SHA512_hash)

SHA3_hash = hashlib.new('sha3_256',name.encode()).hexdigest()
print("SHA3_256", SHA3_hash)

RIPEMD160_hash = hashlib.new('RIPEMD160' ,name.encode()).hexdigest()
print("RIPEMD160", RIPEMD160_hash)



