"""
米家 Token AES解密
獲取的 加密Token 跟 預設使用的Key 為 hex 格式，因此需要先解開hex
Key是固定的，為長度32的0，hex格式。
最後取前面32位，並且以UTF-8解碼，即可得到解密後的Token。

線上工具： http://aes.online-domain-tools.com/
"""
from base64 import b64decode
from Crypto.Cipher import AES
token_Sample = "d10d989a602f43d6ec0f23f373571cf71d9382570aa2a4aee48951c0b12baacb0143db63ee66b0cdff9f69917680151e"
token = ""
while len(token) != 96:
    token = input("輸入長度為96的米家設備token：\n")
MiKey = "00000000000000000000000000000000"
result = AES.new(bytes.fromhex(MiKey), AES.MODE_ECB).decrypt(bytes.fromhex(token))[:32].decode("utf-8")
print("解密後的token:\n{:}".format(result))

