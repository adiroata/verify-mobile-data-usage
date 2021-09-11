#!/usr/bin/python3

from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.exceptions import ResponseErrorLoginCsfrException
import stdiomask
# import json


login = 'admin'
password = stdiomask.getpass('Introduceti parola: ')
# password = '************'
ip = '192.168.8.1'

def main():
    connection = AuthorizedConnection(f'http://{ip}/', login, password)
    
    client = Client(connection)
    response = client.monitoring.month_statistics()
    # dev_signal = client.device.signal()
    # dev_info = client.device.information()

    download = (int(response['CurrentMonthDownload'])//1024000)
    percent = round((download/1000), 2)
    
    print(f"Traffic used: {download} MB | Percent of Quota: {percent} %")
    # print(json.dumps(dev_signal, indent=4))
    # print(json.dumps(dev_info, indent=4))

    client.user.logout()

main()

