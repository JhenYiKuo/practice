import requests
import csv
from datetime import datetime
import pytz
import os

def download_data() ->dict:
    url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=rdec-key-123-45678-011121314&format=JSON'

    response = requests.get(url)
    if response.status_code == 200:
        print('下載成功')
    return response.json()

def jsonDict_csvList(json)->list[dict]:
    '''
    - 傳入json的資料結構
    - 取出需要的資料
    - 組合成list[dict]
    '''
    location = json['cwbopendata']['dataset']['location']
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

def save_csv(data:list[dict],filename) -> bool:
    '''
    - 將lsit[dict]儲存
    - 參數filename要儲存的檔案名稱
    '''
    with open(filename,mode='w',encoding='utf-8',newline='') as file:
        fieldnames = ['城市','起始時間','結束時間','最高溫度','最低溫度','感覺']
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    return True

def get_csvName()->str:
    '''
    - 取得臺灣目前year-month-day.csv
    '''
    taiwan_timezone = pytz.timezone('Asia/Taipei')
    current_date = datetime.now(taiwan_timezone)
    fileName = f'{current_date.year}-{current_date.month}-{current_date.day}.csv'
    return fileName

def get_fileName_path()->str:
    csvFileName = get_csvName()
    current_cwd = os.path.abspath(os.getcwd())
    abs_file_path = os.path.join(current_cwd,'data',csvFileName)
    return abs_file_path

def check_file_exist()->bool:
    abs_file_path = get_fileName_path()
    if os.path.exists(abs_file_path):
        return True
    else:
        return False

if not check_file_exist():
    print('不存在')
    json_data = download_data() #下載資料
    csv_list = jsonDict_csvList(json_data) #解析json的資料成為csv的結構
    is_save= save_csv(csv_list,get_fileName_path()) #儲存資料
    if is_save:
        print('存檔成功')