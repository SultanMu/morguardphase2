import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { APIEndpoints } from "../helpers/app-settings";
@Injectable({
  providedIn: "root",
})
export class FileService {
  constructor(private http: HttpClient) {}

  public listdrives(bucket_name:string): Observable<any> {
  // const headers = new HttpHeaders().set('Cookie',`jwt=${this.jwtToken}`);
  const url = `${APIEndpoints.API_CLIENT}/list-folders/?bucket_name=${encodeURIComponent(bucket_name)}`;
  return this.http.get(url, { withCredentials: true });
  // return this.http.get(url);
  }
  
  public expanddrive(bucket_name:any,uuid:any): Observable<any> {
    const url = `${APIEndpoints.API_CLIENT}/expand-folder/?bucket_name=${encodeURIComponent(bucket_name)}&folder_name=${encodeURIComponent(uuid)}`;
    return this.http.get(url, { withCredentials: true });
  }

  public getFileDetails(filename:string[],bucket_name:any,folder_name:any): Observable<any> {   
    const requestBody = {
      files: [filename],
      bucket_name:bucket_name,
      folder_name:folder_name
    };
  const url = `${APIEndpoints.API_CLIENT}/process-files/`;
  return this.http.post(url,requestBody, {withCredentials: true})
  }
}
