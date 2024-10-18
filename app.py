import sys
import requests
import json

def hello(name):
    try:
        return { "message": "hello, ${name}" }
    except Exception as e:
        print(e)
        return { "is_success": False }

def get_osakametro_station_coords():
    headers = {
        "Content-Type": "application/json;charset=utf-8",
        "Accept": "application/json",
        "X-Api-Key": "XSGUG4p5Ya5vQCehV3zZjaDheZAQMpqP9paVan8W"
    }
    url = "https://static.mobility-operation-info.emetro-app.osakametro.co.jp/emetro/cache/common/json/stationCoords.json"
    response = requests.get(url, headers=headers, timeout=60)
    return response.json()

def main(args = []):
    if(len(args) == 0):
        return

    if(args[0] == 'hello'):
        print("hi!")
        return

    if(args[0] == 'api'):
        response = get_osakametro_station_coords()
        print(response)
        return

if __name__ == "__main__":
    args = sys.argv
    main(args[1:])