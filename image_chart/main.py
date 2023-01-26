import requests
from PIL import Image
from io import BytesIO

url="https://image-charts.com/chart"
payload={
    "chco":"3092de,027182",
    "chd":"t:81,65,50,67,59,81|77,67,10,79,65,77",
    "chdl":"First|Second",
    "chdlp":"b",
    "chs":"480x480",
    "cht":"r",
    "chxt":"r"
}
response=requests.post(url,data=payload)
image=Image.open(BytesIO(response.content))
image.show()