import requests

data = {"group": "ws-group-nieyaoban",
        "action": "base64_encode",
        "encode_str": "HELLO,聂耀攀",
        }

res = requests.post("https://sekiro.virjar.com/invoke", data=data)
print(res.json()['data'])

new_data = {
    "group": "ws-group-nieyaoban",
    "action": "base64_decode",
    "decode_str": "SEVMTE8s6IGC6ICA5pSA",
}

res = requests.post("https://sekiro.virjar.com/invoke", data=new_data)

print(res.json()['data'])
