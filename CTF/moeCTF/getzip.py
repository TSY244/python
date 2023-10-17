import zlib

with open("G:\\CTF\\flag\\5.png","rb") as file:
    data=file.read()
    
zlipData=data[91:]
decompressed_data =zlib.decompress(zlipData)

with open("extracted_data.zlip","w+b") as file:
    file.write(decompressed_data)
    