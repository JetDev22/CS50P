filename = input("File name: ").strip().lower()
if "." in filename:
    filetype = filename.split(".")[-1]
else:
    filetype = ""

images = ["gif", "jpg", "jpeg", "png"]
application = ["pdf", "zip"]
text = ["txt"]

if filetype in images and filetype == "jpg":
    print("image/jpeg")
elif filetype in images and filetype == "jpeg":
    print("image/jpeg")
elif filetype in images:
    print(f"image/{filetype}")
elif filetype in application:
    print(f"application/{filetype}")
elif filetype in text:
    print("text/plain")
else:
    print("application/octet-stream")
