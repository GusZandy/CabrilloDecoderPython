
from cabrillo_decoder import decoder
file = open("cq-ww-cw.cbr")

decoder = decoder.CabrilloDecoder(file)

print(decoder.decode())