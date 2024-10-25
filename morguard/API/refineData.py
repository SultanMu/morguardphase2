import requests
import uuid

def authenticate(username, password, base_url):
    url = f"{base_url}/logon"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'username': username,
        'password': password
    }
    
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        access_token = response.cookies.get('accessToken')
        return access_token
    else:
        raise Exception("Authentication failed", response.text)

def get_form_id(access_token, base_url):
    url = f"{base_url}/property/tab/systemcompany/1?isAdministrationRequest=false"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        forms = response.json()
        for form in forms:
            if form['formName'] == "Target Form Name":  
                return form['formId']
        raise Exception("Form not found")
    else:
        raise Exception("Failed to fetch form IDs", response.text)

def get_property_id(access_token, base_url):
    url = f"{base_url}/properties/asDTO/active"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        properties = response.json()
        for prop in properties:
            if prop['propertyName'] == "Target Property Name": 
                return prop['propertyId']
        raise Exception("Property not found")
    else:
        raise Exception("Failed to fetch property IDs", response.text)

def push_data(access_token, form_id, property_id, data, base_url):
    url = f"{base_url}/property/tab/{form_id}/values/{property_id}"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    json_data = {
        "fieldValues": [
            {"propertyTabFieldId": 1, "value": data['file_name']},      
            {"propertyTabFieldId": 2, "value": data['type']},          
            {"propertyTabFieldId": 3, "value": data['author']},         
            {"propertyTabFieldId": 4, "value": data['company']},        
            {"propertyTabFieldId": 5, "value": data['title']},          
            {"propertyTabFieldId": 6, "value": data['created_date']},   
            {"propertyTabFieldId": 7, "value": data['next_asses_date']},
            {"propertyTabFieldId": 8, "value": data['summary']}         
        ]
    }

    response = requests.post(url, headers=headers, json=json_data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Data push failed", response.text)

def upload_file(access_token, file_path, file_name, mime_type, base_url):
    url = f"{base_url}/amazonclient/uploadfile"
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    files = {
        'file': open(file_path, 'rb'),
        'file_name': (None, file_name),
        's3_file_name': (None, str(uuid.uuid4())),
        'mime_type': (None, mime_type)
    }
    
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("File upload failed", response.text)

def push_to_property_tab(username, password, base_url, file_path, data):
    access_token = authenticate(username, password, base_url)

    form_id = get_form_id(access_token, base_url)
    property_id = get_property_id(access_token, base_url)

    file_name = data['file_name'] + ".pdf"  # Assuming a PDF for now
    mime_type = "application/pdf"
    # upload_file(access_token, file_path, file_name, mime_type, base_url)

    response = push_data(access_token, form_id, property_id, data, base_url)
    print("Data successfully pushed:", response)