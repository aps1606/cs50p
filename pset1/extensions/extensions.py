filename = input("File name: ").lower().strip()

name, filextension = filename.split(".")

if filextension == "gif":
    print("image/gif")

elif filextension == "jpg":
    print("image/jpeg")

elif filextension == "jpeg":
    print("image/jpeg")

elif filextension == "png":
    print("image/png")

elif filextension == "pdf":
    print("application/pdf")

elif filextension == "txt":
    print("text/plain")

elif filextension == "zip":
    print("application/zip")
    
else:
    print("application/octet-stream")

