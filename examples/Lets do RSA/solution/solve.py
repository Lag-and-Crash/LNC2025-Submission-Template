#Just a simple RSA decryption problem. We are given n, e, c and we have to find the flag. We can use the following code to decrypt the message.

from Crypto.Util.number import long_to_bytes
n = 2481463
e = 745799
c = [800295, 1657006, 667668, 323101, 2281490, 323101, 1335034, 743496, 2281490, 2444905, 145243, 33511, 1365638, 426706, 2128075]
p = 2039
q = 1217
# q = n // p
out = ""
for i in c: 
    order = (p-1)*(q-1)
    d = pow(e,-1,order)
    m = pow(i,d,n)
    out += str(long_to_bytes(m).decode("utf-8"))
print(out)
