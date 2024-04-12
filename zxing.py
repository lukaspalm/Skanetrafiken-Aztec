import zxing
reader = zxing.BarCodeReader()
barcode = reader.decode("image5\\full.png")
print(barcode.parsed)