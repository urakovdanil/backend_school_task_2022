import requests
import json


data = [
  {
    "items": [
      {
        "id": 'элемент_12_1',
        "url": "/file/url4",
        "parentId": "элемент_8_1",
        "size": -835,
        "type": "FILE"
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 4,
        "url": "/file/url0",
        "parentId": "элемент_0_4",
        "size": 17,
        "type": "FILE"
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_21_1',
        "url": "/file/url0",
        "parentId": "элемент_01_1",
        "size": 17,
        "type": "FOLDER"
      },
    ],
    "updateDate": "2022-06-02T23:96:40.000Z"
  },
  {
    "items": [
      {
        "id": None,
        "url": "/file/url0",
        "parentId": "элемент_0_7",
        "size": 17,
        "type": "FILE"
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_21_1',
        "url": "/file/url2",
        "parentId": "элемент_0_1",
        "size": 0,
        "type": "FILE"
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_41_1',
        "url": "/file/url03",
        "parentId": "элемент_0_1",
        "size": 9,
        "type": "FOLDER"
      },
    ],
    "updateDate": "2029-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_14_1',
        "url": "/file/url7",
        "parentId": "элемент_0_9",
        "size": 47,
        "type": " folder  "
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_14_1',
        "url": "/file/url0",
        "parentId": "элемент_0_13",
        "size": 48,
        "type": "FOLDER"
      },
    ],
    "updateDate": "2022-36-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_21_1',
        "url": "/file/url02",
        "parentId": "элемент_20_1",
        "size": 2,
        "type": "folder"
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_21_13',
        "url": "/file/url0",
        "parentId": "элемент_0_15",
        "size": 72,
        "type": "FOLDER"
      },
    ],
    "updateDate": "2022-06-65T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_1_1',
        "url": "/file/url0",
        "parentId": "элемент_0_1",
        "size": 7,
        "type": "FOLDER"
      },
    ],
    "updateDate": "2030-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_1_31',
        "url": "/file/url02",
        "parentId": 63,
        "size": 222,
        "type": "FILE"
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_12_1',
        "url": "/file/url01",
        "parentId": "элемент_0_1",
        "size": 17,
        "type": "FOLDER"
      },
    ],
    "updateDate": "2022-06-02T46:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_14_1',
        "url": "/file/url0",
        "parentId": "элемент_03_1",
        "size": 90,
        "type": "FILE "
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_2_1',
        "url": "/file/url0",
        "parentId": "элемент_0_1",
        "size": 17,
        "type": "FOLDER"
      },
    ],
    "updateDate": "2021-02-29T21:50:01.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_21_1',
        "url": "/file/url0",
        "parentId": "элемент_01_1",
        "size": 17,
        "type": "FOLDER"
      },
    ],
    "updateDate": "2022-06-02T23:09:73.000Z"
  },
  {
    "items": [
      {
        "id": 'элемент_12_14',
        "url": 346,
        "parentId": "элемент_10_1",
        "size": 29,
        "type": "FILE"
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": "элемент_62_10",
        # "url": "/file/url0",
        "parentId": None,
        # "size": 16,
        "type": "FOLDER"
      },
      {
        "id": "элемент_62_1",
        "url": "/file/url1",
        "parentId": "элемент_62_10",
        "size": 10,
        "type": "FILE"
      },
      {
        "id": "элемент_62_2",
        "url": "/file/url1",
        "parentId": "элемент_62_10",
        "size": 4,
        "type": "FILE"
      },
      {
        "id": "элемент_62_30",
        # "url": "/file/url1",
        "parentId": "элемент_62_10",
        # "size": 2,
        "type": "FOLDER"
      },
      {
        "id": "элемент_62_4",
        "url": "/file/url2",
        "parentId": "элемент_622_30",
        "size": 1,
        "type": "FILE"
      },
      {
        "id": "элемент_6_5",
        "url": "/file/url2",
        "parentId": "элемент_62_30",
        "size": 1,
        "type": "FILE"
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": "элемент_1_1",
        "url": "/file/url34",
        "parentId": "элемент_12_3",
        "size": 15,
        "type": "FILE"
      },
      {
        "id": "элемент_1_2",
        "url": "/file/url34",
        "parentId": "элемент_12_3",
        "size": 37,
        "type": "FILE"
      }
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": "элемент_62_10",
        # "url": "/file/url0",
        "parentId": None,
        # "size": 16,
        "type": "FOLDER"
      },
      {
        "id": "элемент_62_1",
        "url": "/file/url1",
        "parentId": "элемент_62_10",
        "size": 10,
        "type": "FILE"
      },
      {
        "id": "элемент_62_2",
        "url": "/file/url1",
        "parentId": "элемент_62_10",
        "size": 4,
        "type": "FILE"
      },
      {
        "id": "элемент_62_30",
        # "url": "/file/url1",
        "parentId": "элемент_62_10",
        # "size": 2,
        "type": "FOLDER"
      },
      {
        "id": "элемент_62_4",
        "url": "/file/url2",
        "parentId": "элемент_622_30",
        "size": 1,
        "type": "FILE"
      },
      {
        "id": "элемент_6_5",
        "url": "/file/url2",
        "parentId": "элемент_62_30",
        "size": 1,
        "type": "FILE"
      },
    ],
    "updateDate": "2016-02-29T23:09:40.000Z"
  }
]

API_URL = 'https://pmc-1882.usr.yandex-academy.ru'

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
results = []
f_res = []

for test in data:
    cur_json = json.dumps(test)
    cur_result = requests.post(f'{API_URL}/imports', data=cur_json, headers=headers)
    results.append(cur_result.status_code == 400)

for i in results:
    if results[i] == 'False':
        f_res.append(i)

if all(results):
    print('Correct')
else:
    print("Tests failed")
