#!/usr/bin/env python3

import requests
import json

data1 = {"firstName":"Benediktus", "lastName":"Anindito", "emailId":"bennybroz105@gmail.com"}
data2 = {"firstName":"Maria", "lastName":"Elfrida", "emailId":"elfridamaria@gmail.com"}
data3 = {"firstName":"Maria Ayu", "lastName":"Elfrida", "emailId":"elfridamaria89@gmail.com"}
baseurl = 'http://app:8080'

def testRestApi(scenario):
    if scenario == 1:
        r1 = requests.get(baseurl+'/employees')
        assert r1.json() == [], 'scenario 1 error'
    elif scenario == 2:
        r2 = requests.post(baseurl+'/employees', json=data1)
        data1['id'] = 1
        assert r2.json() == data1, 'scenario 2 error'
    elif scenario == 3:
        r2 = requests.post(baseurl+'/employees', json=data2)
        data2['id'] = 2
        assert r2.json() == data2, 'scenario 3 error'
    elif scenario == 4:
        r1 = requests.get(baseurl+'/employees')
        data1['id'] = 1
        data2['id'] = 2
        assert r1.json() == [data1, data2], 'scenario 4 error'
    elif scenario == 5:
        r2 = requests.get(baseurl+'/employees/1')
        data1['id'] = 1
        assert r2.json() == data1, 'scenario 4 error'
    elif scenario == 6:
        r2 = requests.put(baseurl+'/employees/2', json=data3)
        data3['id'] = 2
        assert r2.json() == data3, 'scenario 5 error'
    elif scenario == 7:
        r2 = requests.delete(baseurl+'/employees/2')
        assert r2.json() == {'deleted':True}, 'scenario 6 error'
    else:
        print('no such scenario')

if __name__ == '__main__':
    for s in range(1,8):
        try:
            testRestApi(s)
        except AssertionError as ae:
            print(ae)
            continue
        else:
            print('scenario {} success'.format(s))

