import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=VJ0wXz47XT8")
img.save("Hol'up, wait a minute.jpg")