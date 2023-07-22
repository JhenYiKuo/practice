import requests
import csv

def download_weather(): #下載weather
    url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=rdec-key-123-45678-011121314&format=JSON'

    respones = requests.get(url)
    if respones.status_code == 200: #檢查是否成功下載
        print('下載成功')
        weather =  respones.json()
        return weather
    else:
        print('下載失敗')
        return False

def parse_json(w): #解析json檔
    location = w['cwbopendata']['dataset']['location']
    weather_list = []
    for item in location:
        city_item = {}
        city_item['城市'] = item['locationName']
        city_item['起始時間']= item['weatherElement'][1]['time'][0]['startTime']
        city_item['結束時間'] = item['weatherElement'][1]['time'][0]['endTime']
        city_item['最高溫度'] = float(item['weatherElement'][1]['time'][0]['parameter']['parameterName'])
        city_item['最低溫度'] = float(item['weatherElement'][2]['time'][0]['parameter']['parameterName'])
        city_item['感覺'] = item['weatherElement'][3]['time'][0]['parameter']['parameterName']
        weather_list.append(city_item)

    return weather_list

def save_csv(data):
    with open('目前天氣.csv',mode='w',encoding='utf-8',newline='') as file:
        fieldnames = ['城市','起始時間','結束時間','最高溫度','最低溫度','感覺']
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    #下載weather
    weather = download_weather()

    if weather != False: #檢查是否下載成功
        print('下載完畢')
    else:
        print('應用程式下載失敗')
        return

    csv_data = parse_json(weather) #解析json檔
    save_csv(csv_data)

if __name__ == '__main__':
    main()