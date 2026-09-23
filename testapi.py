import json

import pytest
from playwright.async_api import Playwright,APIRequestContext

user_json={
  "id": 100,
  "username": "Madhu",
  "firstName":"Madhu",
  "lastName": "Sata",
  "email": "madhu.sata@gmail.com",
  "password":"xyz",
  "phone":"9176856732",
  "userStatus": 0
}


with open('AutomationAmazon/data.json') as json_data_file:
    test_data = json.load(json_data_file)
    data_ret=test_data[('api'
                        'data')]
    print(data_ret)

@pytest.mark.parametrize("extract_all_data",data_ret)
def test_api_user(playwright,extract_all_data):

    #createUser
    api_request_context = playwright.request.new_context(base_url="https://petstore.swagger.io")
    response=api_request_context.post("/v2/user",data=user_json,headers={"content_type":"application/json"})
    assert response.ok


    #getUser
    api_request_context = playwright.request.new_context(base_url="https://petstore.swagger.io")
    response = api_request_context.get(f"/v2/user/{extract_all_data["name"]}", headers={"content_type": "application/json"})
    print(response.json())
    response_body=response.json()
    assert response_body["username"]==extract_all_data["name"]

    # updateUser
    api_request_context = playwright.request.new_context(base_url="https://petstore.swagger.io")
    response = api_request_context.put(f"/v2/user/{extract_all_data["update_user_name"]}",data=user_json,headers={"content_type": "application/json"})
    print(response.json())
    assert response.ok

