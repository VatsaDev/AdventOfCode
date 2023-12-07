import hashlib

i = 0
while True:
    inp = f'bgvyzdsv{i}'
    result = hashlib.md5(inp.encode())
    if result.hexdigest()[:6] == "000000":
        print(i)
        break
    if i%1000==0:
        print(i)
    i+=1