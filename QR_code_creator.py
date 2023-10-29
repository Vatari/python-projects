import pyqrcode

address = input(f'Enter address for QR creation: ')
file_name = input('Enter name for the file: ')

url = pyqrcode.create(address)
url.png(f'{file_name}', scale=8)
