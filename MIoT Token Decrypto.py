"""
米家 Token AES解密
獲取的 加密Token 跟 預設使用的Key 為 hex 格式，因此需要先解開hex
Key是固定的，為長度32的0，hex格式。
最後取前面32位，並且以UTF-8解碼，即可得到解密後的Token。

線上工具： http://aes.online-domain-tools.com/
"""
from base64 import b64decode
from Crypto.Cipher import AES

token = ""
while len(token) != 96:
    token = input("Encrypted MIoT token：\n")
    if len(token) != 96:
      print("Please Input a token, which length is 96.")
MiKey = "00000000000000000000000000000000"
result = AES.new(bytes.fromhex(MiKey), AES.MODE_ECB).decrypt(bytes.fromhex(token))[:32].decode("utf-8")
print("Decrpyted token:\n{:}".format(result))
