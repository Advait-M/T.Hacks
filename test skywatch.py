import requests
import pprint

def main():
    url = 'https://api.skywatch.co/data/'
    query = 'time/2016-07-11,2016-07-12/location/-71.1043443253471,-42.3150676015829,71.1043443253471,-42.3150676015829,71.1043443253471,42.3150676015829,-71.1043443253471,42.3150676015829,-71.1043443253471,-42.3150676015829/source/Landsat-8/level/1/resolution/30/cloudcover/100/band/Blue/'
    headers = { 'Accept': 'application/json', 'x-api-key': '' }
    print("h")
    r = requests.get(url+query, headers=headers)
    if r.status_code < 300:
        pprint.pprint(r.json())
        pprint.pprint(r.request.headers)

if __name__ == '__main__':
    main()
