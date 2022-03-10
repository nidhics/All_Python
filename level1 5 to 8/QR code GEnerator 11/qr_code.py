# Import QRCode from pyqrcode
#pip install pyqrcode
# pip install pypng

import pyqrcode
import png
  
  
# String which represents the QR code
s = "www.google.org"
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8) #scale-->how big your QR code will be
  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)
#png --> portable network graphics, svg --> scalable network graphics, eps ---> encapsulated network graphics