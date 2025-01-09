import requests
from time import time

def get_url(num_request):

    url = 'http://127.0.0.1:8000/get_url'
    json = {"short_url":"PIcFaE"}

    result = requests.get(url, json=json)

    #print(f'Status request {num_request} ->',result.status_code)
    #print('Data response',result.json())


if __name__=='__main__':
    
    start = time()
    
    for i in range(2500):
        get_url(i)

    finish = time()

    print(f'Time taken: {finish-start:.2f} secs')