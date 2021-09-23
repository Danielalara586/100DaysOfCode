# Day 32: QR Generator

import qrcode
from PIL import Image


def qrcode_generator(url: str, image_name: str):
    image = qrcode.make(url)

    image_file = open(image_name, 'wb')
    image.save(image_name)
    image_file.close()

    image_root = './' + image_name
    Image.open(image_root).show()


def run():
    print("Welcome to QR Code Generator!")
    url = input("Please enter a url to be transformed into QR code: ")
    image_name = input("Please enter a name for your generated QR code image: ") + '.png'
    qrcode_generator(url, image_name)


if __name__ == "__main__":
    run()
