"""
Generate wireguard config from cloudflare zero trust
Credit to https://gitlab.com/Misaka-blog/warp-script
"""

import datetime
import json
import random
import string
from urllib import request

"""
Parameters

FAQ:
If "HTTP 401": TOKEN has expired, need a new one
If "HTTP 409": PRIVATE_KEY and PUBLIC_KEY have already been used, need a new pair
"""

# Generate public key with `wg genkey`
PRIVATE_KEY = ""

# Generate public key with `echo <private key> | wg pubkey`
PUBLIC_KEY = ""

# Get the TOKEN manually
TOKEN = ""

# Output filename
OUTPUT_FILENAME = "cf_zero_trust.conf"

"""
Generation
"""

print("Initialising...")
install_id = "".join(random.choices(string.ascii_letters + string.digits, k=22))
fcm_token = f'{install_id}:APA91b{"".join(random.choices(string.ascii_letters + string.digits, k=134))}'

headers = {
    "User-Agent": "okhttp/3.12.1",
    "CF-Client-Version": "a-6.10-2158",
    "Content-Type": "application/json",
    "Cf-Access-Jwt-Assertion": TOKEN,
}

data = {
    "key": PUBLIC_KEY,
    "install_id": install_id,
    "fcm_token": fcm_token,
    "tos": datetime.datetime.now().isoformat()[:-3] + "Z",
    "model": "Linux",
    "name": install_id,  # Or you name it
    "serial_number": install_id,  # Or you name it
    "locale": "zh_CN",
}

req = request.Request(
    "https://api.cloudflareclient.com/v0a2158/reg",
    data=json.dumps(data).encode(),
    headers=headers,
)  # Register with API version v0a2158

print("Generating...")
with request.urlopen(req) as resp:
    v6_addr = json.load(resp)["config"]["interface"]["addresses"]["v6"]
    with open(OUTPUT_FILENAME, "w", newline="") as f:
        for line in [
            "[Interface]",
            f"PrivateKey = {PRIVATE_KEY}",
            f"Address = 172.16.0.2/32, {v6_addr}/128",
            "DNS = 1.1.1.1, 1.0.0.1, 2606:4700:4700::1111, 2606:4700:4700::1001",
            "MTU = 1280",
            "",
            "[Peer]",
            "PublicKey = bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
            "AllowedIPs = 0.0.0.0/0, ::/0",
            "Endpoint = engage.cloudflareclient.com:2408",
        ]:
            f.write(f"{line}\n")
