import requests

def request():

    url = "http://192.168.9.11:9108/docreader/multipart"

    payload={}
    files=[
    ('front',('1hvb1dkqn27vq.jpeg',open('1hvb1dkqn27vq.jpeg','rb'),'image/jpeg')),
    ('back',('1h7whg7vkehps.jpeg',open('1h7whg7vkehps.jpeg','rb'),'image/jpeg'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    #print(response.text)
