# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
from PIL import Image


s=input("Enter the name of the website you want to add to the QR:")


# Generate QR code
url = pyqrcode.create(s)

user1=input("file is created successfully enter the name of the file:")
user=user1+".png"


url.png(user, scale = 6)
print("file is successfully created now opening file")
im=Image.open(user)
im.show()
# Create and save the png file naming "myqr.png"