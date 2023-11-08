import zlib, base64


def compress(read_file, write_file):
    data = open(read_file, 'r').read()  # 32 KB

    # convert data into bytes
    data_bytes = bytes(data, 'utf-8')

    # takes data in term of bytes
    # compress and encode data
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))

    compressed_file = open(write_file, 'w')
    # decode is opposite of bytes
    decoded_data = compressed_data.decode('utf-8')

    # can't save compressed data bytes into txt, the write method takes in string
    compressed_file.write(decoded_data)  # 13 KB


def decompress(compressed_path_file, decompressed_path):
    print(compressed_path_file)
    print(decompressed_path)
    compressed_data = open(compressed_path_file, 'r').read()

    # // decode then de-compress
    decompressed_bytes = zlib.decompress(base64.b64decode(compressed_data))
    decompressed_data = decompressed_bytes.decode('utf-8')

    decompress_file = open(decompressed_path, 'w')
    decompress_file.write(decompressed_data)
