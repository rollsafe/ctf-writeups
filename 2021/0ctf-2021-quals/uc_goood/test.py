from pwn import *

MAIN = b'\x48\x83\xec\x20\x66\xc7\x44\x24\x0e\x00\x00\x48\x8d\x5c\x24\x0e\x48\xc7\x44\x24\x10\x00\x00\x00\x00\x48\xc7\x44\x24\x18\x00\x00\x00\x00\xb9\x41\x00\x00\x00\x48\x8d\x15\x8b\x01\x00\x00\xbe\x01\x00\x00\x00\x31\xc0\xbf\x01\x00\x00\x00\xe8\xbb\x01\x00\x00\xb9\x02\x00\x00\x00\x48\x89\xda\x31\xf6\x31\xff\x31\xc0\xe8\xa8\x01\x00\x00\x8a\x44\x24\x0e\x3c\x32\x74\x39\x3c\x33\x74\x62\x3c\x31\x0f\x85\x04\x01\x00\x00\xb9\x12\x00\x00\x00\x48\x8d\x15\x35\x01\x00\x00\xbe\x01\x00\x00\x00\x31\xc0\xbf\x01\x00\x00\x00\xe8\x77\x01\x00\x00\x48\x83\xc4\x20\x48\xbf\x00\xf8\xee\xdb\xea\x0d\x00\x00\xff\x27\xb9\x12\x00\x00\x00\x48\x8d\x15\xf6\x00\x00\x00\xbe\x01\x00\x00\x00\x31\xc0\xbf\x01\x00\x00\x00\xe8\x4a\x01\x00\x00\x48\x83\xc4\x20\x48\xbf\x00\xf8\xee\xdb\xea\x0d\x00\x00\xff\x27\xb9\x07\x00\x00\x00\x48\x8d\x15\xc2\x00\x00\x00\xbe\x01\x00\x00\x00\x31\xc0\xbf\x01\x00\x00\x00\xe8\x1d\x01\x00\x00\x31\xf6\x31\xff\x48\x8d\x54\x24\x10\xb9\x08\x00\x00\x00\x31\xc0\xe8\x08\x01\x00\x00\xb9\x07\x00\x00\x00\xbe\x01\x00\x00\x00\x31\xc0\x48\x8d\x15\x82\x00\x00\x00\xbf\x01\x00\x00\x00\xe8\xeb\x00\x00\x00\x31\xf6\x31\xff\x31\xc0\x48\x8d\x54\x24\x18\xb9\x08\x00\x00\x00\xe8\xd6\x00\x00\x00\x48\x81\x7c\x24\x18\xff\x00\x00\x00\x0f\x87\xef\xfe\xff\xff\xb9\x07\x00\x00\x00\x48\x8d\x15\x41\x00\x00\x00\xbe\x01\x00\x00\x00\x31\xc0\xbf\x01\x00\x00\x00\xe8\xaa\x00\x00\x00\x48\x8b\x4c\x24\x18\x31\xf6\x31\xff\x48\x8b\x54\x24\x10\x31\xc0\xe8\x95\x00\x00\x00\xe9\xb8\xfe\xff\xff\xbe\xff\x00\x00\x00\xbf\x3c\x00\x00\x00\x31\xc0\xe8\x7f\x00\x00\x00\xe9\xa2\xfe\xff\xff\x64\x61\x74\x61\x3a\x20\x00\x73\x69\x7a\x65\x3a\x20\x00\x61\x64\x64\x72\x3a\x20\x00\x50\x61\x74\x68\x65\x74\x69\x63\x20\x68\x75\x6d\x61\x6e\x20\x3e\x0a\x00\x50\x6f\x77\x65\x72\x66\x75\x6c\x20\x61\x64\x6d\x69\x6e\x20\x3e\x0a\x00\x57\x65\x6c\x63\x6f\x6d\x65\x20\x74\x6f\x20\x75\x63\x5f\x67\x6f\x6f\x6f\x64\x0a\x31\x2e\x20\x61\x64\x6d\x69\x6e\x20\x74\x65\x73\x74\x0a\x32\x2e\x20\x75\x73\x65\x72\x20\x74\x65\x73\x74\x0a\x33\x2e\x20\x70\x61\x74\x63\x68\x20\x64\x61\x74\x61\x0a\x3f\x3a\x20\x00\x48\x89\xf8\x48\x89\xf7\x48\x89\xd6\x48\x89\xca\x4d\x89\xc2\x4d\x89\xc8\x4c\x8b\x4c\x24\x08\x0f\x05\xc3'
with open('main', 'wb') as f:
    f.write(MAIN)
ADMIN = b'\xb9\x10\x00\x00\x00\x48\x8d\x15\x37\x00\x00\x00\x31\xc0\xbe\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x48\x83\xec\x08\xe8\x5f\x00\x00\x00\x48\x8d\x05\x2b\x00\x00\x00\x48\xa3\x33\xe2\xaf\xec\xab\x0b\x00\x00\x48\x83\xc4\x08\x48\xbf\x00\xf8\xee\xdb\xea\x0d\x00\x00\xff\x67\x08\x49\x6d\x61\x67\x69\x6e\x61\x74\x69\x6f\x6e\x20\x69\x73\x20\x00\x6b\x33\x33\x6e\x6c\x61\x62\x65\x63\x68\x6f\x20\x27\x6d\x6f\x72\x65\x20\x69\x6d\x70\x6f\x72\x74\x61\x6e\x74\x20\x74\x68\x61\x6e\x20\x6b\x6e\x6f\x77\x6c\x65\x64\x67\x65\x2e\x27\x00\x48\x89\xf8\x48\x89\xf7\x48\x89\xd6\x48\x89\xca\x4d\x89\xc2\x4d\x89\xc8\x4c\x8b\x4c\x24\x08\x0f\x05\xc3'.ljust(0x1000, b'\xf4')
with open('admin', 'wb') as f:
    f.write(ADMIN)

TAIL = b'\x31\xc0\xb9\x32\x00\x00\x00\x48\x8d\x15\x55\x00\x00\x00\xbe\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x48\x83\xec\x18\x66\x89\x44\x24\x0e\x31\xc0\xe8\x6d\x00\x00\x00\x31\xf6\x31\xff\x31\xc0\x48\x8d\x54\x24\x0e\xb9\x02\x00\x00\x00\xe8\x58\x00\x00\x00\x80\x7c\x24\x0e\x79\x75\x11\x48\x83\xc4\x18\x48\xbf\x00\xf8\xee\xdb\xea\x0d\x00\x00\xff\x67\x10\x31\xf6\xbf\x3c\x00\x00\x00\x31\xc0\xe8\x32\x00\x00\x00\x43\x6f\x6e\x67\x72\x61\x74\x75\x6c\x61\x74\x69\x6f\x6e\x73\x21\x20\x54\x65\x73\x74\x20\x73\x75\x63\x63\x65\x65\x64\x21\x0a\x54\x72\x79\x20\x61\x67\x61\x69\x6e\x3f\x20\x28\x79\x2f\x5b\x6e\x5d\x29\x00\x48\x89\xf8\x48\x89\xf7\x48\x89\xd6\x48\x89\xca\x4d\x89\xc2\x4d\x89\xc8\x4c\x8b\x4c\x24\x08\x0f\x05\xc3'
with open('tail', 'wb') as f:
    f.write(TAIL)

arr = []
for al in range(0x100):
    v = al
    al += ADMIN[al] + 1
    al &= 0xFF

    if 0x80 <= al < 0x99:
        print(v, hex(al))
        arr.append(v)

context.arch = "amd64"
for al in arr:
    v = al
    tmp = bytearray(ADMIN)
    al += tmp[al] + 1
    al &= 0xFF
    tmp[al] = (tmp[al] + al) & 0xFF

    print(v, al, tmp[al])
    print(disasm(tmp[0x80:0xa0]))
