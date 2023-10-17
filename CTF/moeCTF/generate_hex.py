with open("hex.txt", "w") as f:
    for i in range(0x10000):
        f.write("{:04x}".format(i) + "\n")
