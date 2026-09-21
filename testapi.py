
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



def test_api_user(playwright):


    api_request_context = playwright.request.new_context(base_url="https://petstore.swagger.io")
    response=api_request_context.post("/v2/user",data=user_json,headers={"content_type":"application/json"})
    assert response.ok

    name="Madhu"
    api_request_context = playwright.request.new_context(base_url="https://petstore.swagger.io")
    response = api_request_context.get(f"/v2/user/{name}", headers={"content_type": "application/json"})
    print(response.json())
    response_body=response.json()
    assert response_body["username"]==name


    update_user_name="Teresa"

    api_request_context = playwright.request.new_context(base_url="https://petstore.swagger.io")
    response = api_request_context.put(f"/v2/user/{update_user_name}",data=user_json,headers={"content_type": "application/json"})
    print(response.json())
    assert response.ok





