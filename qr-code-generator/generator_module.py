import pyqrcode


def generate_qr_code(name, link):
    filename = name + ".png"
    # qr code from link
    url = pyqrcode.create(link)
    url.png(filename, scale=8)
    return filename
