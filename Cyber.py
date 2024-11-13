import base64

fin = open("")
fout = open("")

for line in fin:
    encoded_data = line.rstrip()
    decoded_data = base64.b64decode(encoded_data)
    fout.write(str(decoded_data))

fin.close()
fout.close()
