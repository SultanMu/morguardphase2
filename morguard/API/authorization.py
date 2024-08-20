import requests
class Credentials:
    def __init__(self,client_id:str,client_secret:str,tenant_id:str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
    def auth(self):
        data = {'grant_type':"client_credentials",
                'client_id':self.client_id,
                'client_secret':self.client_secret,
                'resource':"https://graph.microsoft.com/"}
        response = requests.post(url="https://login.microsoftonline.com/{}/oauth2/token".format(self.tenant_id),data=data)
        if response.status_code == 200:
            return response
        else:
            raise Exception("Failed to acquire access token, status code : "+str(response.status_code))
        
