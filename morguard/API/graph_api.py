import requests
class GraphAPI:
    def __init__(self,bearer_token:str):
        self.credentials = bearer_token
    def search(self,site_name:str):
        headers = {"Authorization": "Bearer {}".format(self.credentials)}
        response = requests.get("https://graph.microsoft.com/v1.0/sites?search={}".format(site_name),headers=headers)
        if response.status_code == 200:
            return response
        else:
            raise Exception("Failed to search site by keyword status code : ".format(str(response.status_code)))
    def list_drives(self,site_id:str):
        headers = {"Authorization": "Bearer {}".format(self.credentials)}
        response = requests.get("https://graph.microsoft.com/v1.0/sites/{}/drives/".format(site_id),headers=headers)
        if response.status_code == 200:
            drives = {}
            for drive in response.json()["value"]:
                drives[drive["name"]] = drive["id"]
            return drives
        else:
            raise Exception("Failed to list drives status code : ".format(str(response.status_code)))
        
    def expand_drive(self,site_id:str,drive_id:str):
        headers = {"Authorization": "Bearer {}".format(self.credentials)}
        response = requests.get("https://graph.microsoft.com/v1.0/sites/{}/drives/{}/root/children/".format(site_id,drive_id),headers=headers)
        if response.status_code == 200:
            files = {}
            for file in response.json()["value"]:
                files[file["name"]] = file["@microsoft.graph.downloadUrl"]
            return files
        else:
            raise Exception("Failed to expand drives status code : ".format(str(response.status_code)))
        
