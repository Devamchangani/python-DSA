import pyqrcode
import png
from pyqrcode import QRCode

s = "" # Enter your Link

url = pyqrcode.create(s)

url.png('myqr.png', scale = 6)