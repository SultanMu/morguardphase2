import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Client, Company, CompanyProfile, UserProfile } from '../model/Userprofile'
import { AytHttpParams } from '../helpers/http-config';
import { APIEndpoints } from '../helpers/app-settings';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http:HttpClient) { }

  public authLogin(): Observable<any> {
    let options = {};
    return this.http.get<any>(`http://20.220.133.246:8000/client/authorize/`, options);
  }

  public registerUser(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.API_CLIENT}/register/`, obj, options)
  }

  public loginUser(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.API_CLIENT}/login/`, obj, options);
  }

  /////////xcv endpoints///////

  public getAccountBills(id:any): Observable<any> {
    let options = {};
    return this.http.get<any>(`http://localhost:3000/users`, options);
  }

  public validateRecruiter(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any>(`${APIEndpoints.RECRUITER_API}/validate_recruiter/`, options);
  }

  public confirmConsent(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any>(`${APIEndpoints.RECRUITER_API}/consent/`, options);
  }

  public requestConsent(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.RECRUITER_API}/consent/`, obj, options)
  }

  public deleteRecruiter(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.delete<any>(`${APIEndpoints.RECRUITER_API}/delete_recruiter/`, options);
  }

  public deleteClient(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.delete<any>(`${APIEndpoints.CLIENT_API}/delete-client/`, options);
  }

  public resendEmail(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.RECRUITER_API}/resend_email/`, obj, options)
  }

  public notifyPricing(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any>(`${APIEndpoints.RECRUITER_API}/notify-pricing/`, options)
  }

  public getCompanyProfile(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any>(`${APIEndpoints.RECRUITER_API}/company_profile/`, options);
  }

  public verifyPaymentDetails(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    

    return this.http.get<any>(`${APIEndpoints.RECRUITER_API}/verify_payment_details/`, options);
  }

  public loginCompany(params?: AytHttpParams): Observable<Company> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<Company>(`${APIEndpoints.RECRUITER_API}/login_company/`, options);
  }

  public registerRecruiter(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.RECRUITER_API}/register_recruiter/`, obj, options)
  }

  public getRecruiterClients(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any>(`${APIEndpoints.RECRUITER_API}/get_clients/`, options);
  }

  public deleteAlignedJD(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.delete<any>(`${APIEndpoints.RECRUITER_API}/delete_jd/`, options);
  }

  public passwordResetRecruiter(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any>(`${APIEndpoints.RECRUITER_API}/reset_password/`, options);
  }

  public createRecruiter(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.RECRUITER_API}/recruiter-create/ `, obj, options)
  }

  public createCompany(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.RECRUITER_API}/company_create/ `, obj, options)
  }

  public passwordUpdateRecruiter(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.RECRUITER_API}/update_password/ `, obj, options)
  }

  public submitVanity(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.CLIENT_API}/process/ `, obj, options)
  }

  public updateTokens(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any>(`${APIEndpoints.GPT_API}/update-tokens/`, options);
  }

  public cancelSubscriptionPlan(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.CLIENT_API}/cancel-plan/ `, obj, options)
  }

  public checkoutStripe(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any>(`${APIEndpoints.CLIENT_API}/verify-plan/`, options);
  }

  public verifyVanity(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any>(`${APIEndpoints.CLIENT_API}/verify-vanity`, options);
  }

  public parsePDF(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.CLIENT_API}/parseLinkedinPdf `, obj, options)
  }

  public verifyPaymentPlan(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any>(`${APIEndpoints.CLIENT_API}/verify-plan/`, options);
  }

  public getPaymentHistory(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any>(`${APIEndpoints.RECRUITER_API}/get-payment-history/`, options);
  }

  public getClient(params?: AytHttpParams): Observable<Client> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<Client>(`${APIEndpoints.CLIENT_API}/get-client/`, options);
  }

  public getAllClients(params?: AytHttpParams): Observable<any[]> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any[]>(`${APIEndpoints.CLIENT_API}/process`, options);
  }

  public getAllResumes(params?: AytHttpParams): Observable<any[]> {
      let options = {};
      if (params) {
        options = { params: params.getParams() };
      }    
      return this.http.get<any[]>(`${APIEndpoints.CLIENT_API}/listResumes/`, options);
  }

  public getIndividualResume(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    // return this.http.get<any>(`${APIEndpoints.CLIENT_API}/specificResume`, options);
    return this.http.get<any>(`${APIEndpoints.CLIENT_API}/specificResume/`, options);
  }

  public getResumeDetails(params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.get<any>(`${APIEndpoints.CLIENT_API}/fetchResume/`, options);
  }

  public updateResume(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.CLIENT_API}/update/ `, obj, options)
  }

  public getnerateChatGPT(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.GPT_API}/refine/ `, obj, options)
  }

  // public getREsumeDetails() {
  //   this.http.get<any>('http://127.0.0.1:8000/client/fetchResume?public_id=sherin-atapattu-9b99b5131').subscribe(res => {
  //     this.resumeData(res)

  //   }, err => {
  //     alert("Something went wrong")
  //   })
  // }

  public updateUserprofile(user:UserProfile,payload:any): Observable<UserProfile> {
    let options = {};
    return this.http.patch<UserProfile>(`http://localhost:3000/resume/${user.id}`, payload);
  }

  public alignJD(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.GPT_API}/jdalign/ `, obj, options)
  }
  public getCoverletter(obj:any, params?: AytHttpParams): Observable<any> {
    let options = {};
    if (params) {
      options = { params: params.getParams() };
    }    
    return this.http.post<any>(`${APIEndpoints.GPT_API}/get_coverLetter/ `, obj, options)
  }

  public sendSupportMessage(payload:any): Observable<any> {
    return this.http.post<any>(`${APIEndpoints.RECRUITER_API}/post-ticket/ `, payload)
  }
}
