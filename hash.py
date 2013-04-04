import skein
from gmpy import hamdist as hamming
import binascii
import os

urandom = open("/dev/urandom", "rb")
def somebits():
    return binascii.hexlify(urandom.read(512))

if __name__ == "__main__":
    original = int("5b4da95f5fa08280fc9879df44f418c8f9f12ba424b7757de02bbdfbae0d4c4fdf9317c80cc5fe04c6429073466cf29706b8c25999ddd2f6540d4475cc977b87f4757be023f19b8f4035d7722886b78869826de916a79cf9c94cc79cd4347d24b567aa3e2390a573a373a48a5e676640c79cc70197e1c5e7f902fb53ca1858b6", 16)
    domain = "bristol.ac.uk"
    best = 415
    best_actual = 1000
    i = 0
    while True:
        i += 1
        if i % (1 << 16) == 0:
            print("actual",best_actual,i)
            print(best)
        bits = somebits()
        sbits = "".join([chr(byte) for byte in bits])
        test = skein.skein1024(bits).hexdigest()
        as_bits = int(test, 16)
        distance = hamming(as_bits, original)
        if distance < best_actual:
            print("actual",distance,i)
            best_actual = distance
        if distance < best:
            print( "-------------")
            best = distance
            print(best)
            os.system('curl -s "http://almamater.xkcd.com/?edu=bristol.ac.uk" --data "hashable=' + sbits + '"')
            print("")
            print("")
            print("")
            print("")
            print(test)
            print("-------------")
