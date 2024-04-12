import zlib

with open('image5\\hexfile', 'rb') as f:
    data = f.read()
print(data)
decompressed = zlib.decompress(b"78 5e 5b c2 94 58 c3 a6 c2 94 68 c2 98 58 10 c3 89 58 c3 95 1c c3 a1 c2 b0 24 c2 b1 c2 a4 c3 80 c3 88 c3 80 c3 88 c3 84 c3 80 c3 84 c3 90 30 c3 84 c3 80 c3 94 c3 90 c3 82 c3 80 34 2a 39 31 27 3d c3 93 23 c3 98 c3 88 c3 94 4c c3 97 c3 90 c3 88 22 39 3b 33 25 c3 8b 27 2b c2 a2 28 c3 9f c3 9d c3 89 c2 b3 c3 92 34 39 05 c3 88 c3 b5 c3 8b 4a c2 ae c3 b4 c2 ad 72 34 c3 b2 73 c2 8c 64 54 6e c2 8e 08 5a 0e c3 92 c2 92 c3 aa 0a c3 92 c2 92 c2 9c c2 99 c2 99 c2 92 64 68 00 c3 91 c2 95 c2 9d 11 c3 a0 54 14 c2 9a 16 c2 94 c2 93 c2 9c c2 9b 59 c2 96 68 c2 92 c2 9c 5a 51 00 c2 b1 c3 8d c3 94 c3 80 3c c3 84 c3 88 c3 88 c3 88 c3 82 c3 84 32 2a 39 c2 a5 c2 b8 00 c2 a4 21 c2 a5 38 13 c3 89 c3 9c c2 88 c2 ae c2 85 40 c3 81 c3 86 c2 a5 29 c3 89 c3 b1 65 79 c2 89 c2 86 20 2a 17 42 c2 95 c2 80 c2 a9 c3 9c c2 94 c2 a6 c2 85 c3 89 25 c2 99 29 c3 a9 2e c2 be c3 86 4e 16 7e 51 40 4e 41 72 c3 a3 c2 a2 c3 a4 c3 a4 c3 84 c2 92 c3 a4 c3 8a c3 bc c3 92 c3 a4 c2 92 c2 a2 44 c2 b0 c2 ba c2 92 c3 a4 0a 07 43 03 2b 07 c2 b0 c2 ad c3 86 46 40 5b c2 8d 0d 0c c2 a2 c3 b4 21 5e 36 36 00 3a 02 c3 88 55 50 53 c3 90 50 2e 4e 4e c3 8c c3 8b 4c 54 c2 a8 51 50 2e 4b c3 8d c3 93 04 0a 29 c2 97 c2 a7 c2 a6 66 c2 a7 24 56 16 47 38 64 c3 b5 c3 bd c3 ba c2 b0 c3 bf c2 aa c3 aa 57 c3 8b c3 ae c3 8b 35 c3 8d 02 c3 a6 19 7f 66 c2 ae c2 9c c2 b8 c3 a3 c3 97 c3 9d c3 90 63 7a c3 97 c2 af c3 bc c2 b5 3e 7b c3 aa c2 85 4e c2 8b 5f 3a c3 87 73 57 59 29 c3 9d c2 82 c2 a8 c3 a5 c3 a7 c2 bc c3 b7 3e 6b c3 99 51 55 c2 bb c2 bb c3 83 c3 b1 c2 b1 c2 8d c2 9d 16 c3 ab c2 b5 c2 9e 00 c3 89 18 c2 a9 09 62 c2 8b c3 8a 4b c2 b5 c3 9d c2 9a c3 af 05 6e 69 7c 02 00 6b c2 b8 c2 8f 73 0a")
print(decompressed)