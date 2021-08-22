# file capacity on disk

while True:
    try:
        byte = int(input("What is your file size (byte): "))
        if byte > 0:
            break
        else:
            print("File size shall be greater than 0")
            print()
    except ValueError:
        print("File size shall be integer type, not float type or string")
        print()

kb = (byte // 4096 + (byte % 4096 > 0)) * 4
print(f"{byte} byte(s) occupied {kb} KB on the disk")