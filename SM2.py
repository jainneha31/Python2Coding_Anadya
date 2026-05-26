import random
letters='abcdefghijklmnopqrstuvwxyz'

def even_odd_swap(x):
    if len(x)%2!=0:
        x = x + ' '

    even_letters = x[0::2]
    odd_letters  = x[1::2]
    s=''

    for i in range(len(even_letters)):
        s = s+odd_letters[i]
        s = s+even_letters[i]
    
    return s

def swap_middle(x):
    if len(x)%2!=0:
        x = x + ' '

    first_half = x[0:int(len(x)/2):1]
    second_half = x[int(len(x)/2)::1]
    
    s = ''
    s = s + second_half 
    s = s + first_half
    return s
    
def reverse(x):
    s = x[::-1]
    return s

def swap_mid_rev(x):
    s_swap = swap_middle(x)
    s = reverse(s_swap)
    return s

def swap_mid_rev_decode(x):
    s_rev = reverse(x)
    s = swap_middle(s_rev)
    return s

def reverse_word(x):
    words = x.split(' ')
    s = ''
    for kk in range(len(words)):
        s = s+reverse(words[kk])+' '
    return s

def caesar_cipher(x, n):   
    s=''
    for i in range(len(x)):
        if x[i] == ' ':
            s = s + ' '
        else:
            idx = letters.find(x[i])
            new_idx = (idx+n)%26
            s = s + letters[new_idx]
    return s        

print()
print()


headers_list =['python', 'cobras', 'snakes']
hdr = random.choice(headers_list)
secret_code = ''

for kk in range(10):
    n = random.randint(0, 25)
    secret_code = secret_code + letters[n]

msg = hdr + secret_code

encoder = random.randint(0, 3)

if encoder == 0:
    msg_enc = msg
elif encoder == 1:
    msg_enc = even_odd_swap(msg)
elif encoder == 2:
    msg_enc = reverse(msg)
else:
    msg_enc = swap_middle(msg)

msg_enemy = caesar_cipher(msg_enc, random.randint(1, 25))
print()
print('I am hearing ...')
print(msg_enemy)
print()

header_len = len(headers_list[0])

def find_header(msg_fun):
    codeBroken = False
    secret_code = ''
    for hdr in headers_list:
        if msg_fun.find(hdr) == 0:
            print('Header Found:' + hdr)
           
            secret_code = msg_fun[len(hdr):len(hdr)+10:1]
            codeBroken = True
            break

    return codeBroken, secret_code


codeBroken = False

for kk in range(1, 26):
    msg_dec = caesar_cipher(msg_enemy, kk)
    msg_dec_eo = even_odd_swap(msg_dec)
    msg_dec_r  = reverse(msg_dec)
    msg_dec_ms = swap_middle(msg_dec)

    codeBroken, secret_code = find_header(msg_dec)

    if codeBroken:
        print('Secret code is ...')
        print(secret_code)
        break

    codeBroken, secret_code = find_header(msg_dec_eo)
    
    if codeBroken:
        print('Secret code is ...')
        print(secret_code)
        break

    codeBroken, secret_code = find_header(msg_dec_r)
    
    if codeBroken:
        print('Secret code is ...')
        print(secret_code)
        break

    codeBroken, secret_code = find_header(msg_dec_ms)
    
    if codeBroken:
        print('Secret code is ...')
        print(secret_code)
        break

    for hdr in headers_list:
        if msg_dec.find(hdr) == 0:
            print('Header Found:' + hdr)
            print('Secret code is ...')
            print(msg_dec[len(hdr):len(hdr)+10:1])
            codeBroken = True
            break
        
        

    if msg_dec[0:header_len:1] in headers_list:
        print('code cracked ...')

        print('Secret code is ...')
        print(msg_dec[header_len::1])
        break
    elif msg_dec_eo[0:header_len:1] in headers_list:
        print('code cracked ...')

        print('Secret code is ...')
        print(msg_dec_eo[header_len::1])
        break
    elif msg_dec_r[0:header_len:1] in headers_list:
        print('code cracked ...')
 
        print('Secret code is ...')
        print(msg_dec_r[header_len::1])
        break
    elif msg_dec_ms[0:header_len:1] in headers_list:
        print('code cracked ...')
       
        print('Secret code is ...')
        print(msg_dec_ms[header_len::1])
        break

