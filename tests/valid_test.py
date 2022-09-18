import requests
import json


valid_data = [
  {
    "items": [
      {
        "id": "элемент_15_20",
        # "url": "/file/url0",
        "parentId": None,
        # "size": 18,
        "type": "FOLDER"
      },
      {
        "id": "элемент_15_10",
        "url": "/file/url1",
        "parentId": "элемент_15_20",
        "size": 13,
        "type": "FILE"
      },
      {
        "id": "элемент_15_12",
        # "url": "/file/url1",
        "parentId": "элемент_15_20",
        # "size": 5,
        "type": "FOLDER"
      },
      {
        "id": "элемент_15_13",
        "url": "/file/url2",
        "parentId": "элемент_15_12",
        "size": 3,
        "type": "FILE"
      },
      {
        "id": "элемент_15_14",
        "url": "/file/url2",
        "parentId": "элемент_15_12",
        "size": 2,
        "type": "FILE"
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": "элемент_23_14",
        "url": "/file/url2",
        "parentId": "элемент_23_97",
        "size": 2,
        "type": "FILE"
      },
      {
        "id": "элемент_23_97",
        # "url": "/file/url0",
        "parentId": None,
        # "size": 2,
        "type": "FOLDER"
      }
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": "элемент_34_0",
        # "url": "/file/url0",
        "parentId": None,
        # "size": 234,
        "type": "FOLDER"
      },
      {
        "id": "элемент_34_1",
        "url": "/file/url1",
        "parentId": "элемент_34_0",
        "size": 234,
        "type": "FILE"
      },
      {
        "id": "элемент_34_2",
        # "url": "/file/url1",
        "parentId": "элемент_34_0",
        # "size": 0,
        "type": "FOLDER"
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  },
  {
    "items": [
      {
        "id": "элемент_41_3",
        # "url": "/file/url0",
        "parentId": None,
        # "size": 20,
        "type": "FOLDER"
      },
      {
        "id": "элемент_41_1",
        "url": "/file/url1",
        "parentId": "элемент_41_3",
        "size": 16,
        "type": "FILE"
      },
      {
        "id": "элемент_4_22",
        # "url": "/file/url1",
        "parentId": "элемент_41_3",
        # "size": 4,
        "type": "FOLDER"
      },
      {
        "id": "элемент_4_3",
        "url": "/file/url2",
        "parentId": "элемент_4_22",
        "size": 4,
        "type": "FILE"
      },
    ],
    "updateDate": "2022-06-02T23:09:40.000Z"
  }
]

API_URL = 'https://pmc-1882.usr.yandex-academy.ru'

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
results = []

for test in valid_data:
    cur_json = json.dumps(test)
    cur_result = requests.post(f'{API_URL}/imports', data=cur_json, headers=headers)
    results.append(cur_result.status_code == 200)

for test in invalid_data:
    cur_json = json.dumps(test)
    cur_result = requests.post(f'{API_URL}/imports', data=cur_json, headers=headers)
    results.append(cur_result.status_code == 400)

if all(results):
    print('Correct')
else:
    print("Not correct")
