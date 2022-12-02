from cabrillo_decoder import decoder
file = open("cq-ww-cw.cbr")

cabrillo = decoder.Cabrillo(file)

print(cabrillo.decode())