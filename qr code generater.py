import qrcode
qr=qrcode.make('please view my profile')
data="https://www.linkedin.com/in/saikumar9966"
qr=qrcode.make(data)
qr.save("docpy.png")
qr.show()