import qrcode

email_address = "bharatiyogesh67@gmail.com"
subject = "my"
body = "hello"
mailto = f"mailto:{email_address}?subect={subject}&body={body}"
img = qrcode.make(mailto)
type(img)
img.save("email.png")