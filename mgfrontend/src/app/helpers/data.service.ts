import { Injectable } from '@angular/core';
import { AppUser, Client, PaymentHistory, SubscriptionDetails, SubscriptionPlan } from 'app/model/Userprofile';
import { Subject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private dataSubject = new Subject<string>();
  private nameSubject = new Subject<string>();
  private vanitySubject = new Subject<string>();
  private subscriptionSubject = new Subject<SubscriptionPlan>();
  private SubscriptionDetailsSubject = new Subject<SubscriptionDetails>();
  private PaymentHistorySubject = new Subject<PaymentHistory>();
  private clientSubject = new Subject<Client>();
  private appUserSubject = new Subject<AppUser>();
  private userTypeSubject = new Subject<string>();
  private reloadTemplateSubject = new Subject<string>();
  private previewVisbleSubject = new Subject<string>();
  private previewSaveSubject = new Subject<string>();
  private goToJDAlignSubject = new Subject<string>();
  private selectTemplateSubject = new Subject<string>();
  private removeTemplateSubject = new Subject<string>();
  private hidePreviewSubject = new Subject<string>();
  private pdfPreviewSubject = new Subject<string>();
  private removePdfPreviewSubject = new Subject<string>();
  private pdfDownloadSubject = new Subject<string>();
  private JDDataSubject :any;
  
  constructor() { }


  setPdfDownload(data: string) {
    this.pdfDownloadSubject.next(data);
  }

  getPdfDownload(): Observable<string> {
    return this.pdfDownloadSubject.asObservable();
  }



  setRemovePdfPreview(data: string) {
    this.removePdfPreviewSubject.next(data);
  }

  getRemovePdfPreview(): Observable<string> {
    return this.removePdfPreviewSubject.asObservable();
  }



  setPdfPreview(data: string) {
    this.pdfPreviewSubject.next(data);
  }

  getPdfPreview(): Observable<string> {
    return this.pdfPreviewSubject.asObservable();
  }

  

  setHidePreview(data: string) {
    this.hidePreviewSubject.next(data);
  }

  getHidePreview(): Observable<string> {
    return this.hidePreviewSubject.asObservable();
  }




  setRemoveTemplate(data: string) {
    this.removeTemplateSubject.next(data);
  }

  getRemoveTemplate(): Observable<string> {
    return this.removeTemplateSubject.asObservable();
  }


  setSelectTemplate(data: string) {
    this.selectTemplateSubject.next(data);
  }

  getSelectTemplate(): Observable<string> {
    return this.selectTemplateSubject.asObservable();
  }




  setGoToJDAlign(data: string) {
    this.goToJDAlignSubject.next(data);
  }

  getGoToJDAlign(): Observable<string> {
    return this.goToJDAlignSubject.asObservable();
  }



  setPreviewSave(data: string) {
    this.previewSaveSubject.next(data);
  }

  getPreviewSave(): Observable<string> {
    return this.previewSaveSubject.asObservable();
  }



  

  setPreviewVisble(data: string) {
    this.previewVisbleSubject.next(data);
  }

  isPreviewVisble(): Observable<string> {
    return this.previewVisbleSubject.asObservable();
  }



  setReloadTemplate(data: string) {
    this.reloadTemplateSubject.next(data);
  }

  getReloadTemplate(): Observable<string> {
    return this.reloadTemplateSubject.asObservable();
  }

  setData(data: string) {
    this.dataSubject.next(data);
  }
  
  getData(): Observable<string> {
    return this.dataSubject.asObservable();
  }

  setName(data: string) {
    this.nameSubject.next(data);
  }
  
  getName(): Observable<string> {
    return this.nameSubject.asObservable();
  }

  setVanity(data: string) {
    this.vanitySubject.next(data);
  }
  
  getVanity(): Observable<string> {
    return this.vanitySubject.asObservable();
  }

  setSubscriptionPlan(data: SubscriptionPlan) {
    this.subscriptionSubject.next(data);
  }
  
  getSubscriptionPlan(): Observable<SubscriptionPlan> {
    return this.subscriptionSubject.asObservable();
  }

  setSubscriptionDetails(data: SubscriptionDetails) {
    this.SubscriptionDetailsSubject.next(data);
  }
  
  getSubscriptionDetails(): Observable<SubscriptionDetails> {
    return this.SubscriptionDetailsSubject.asObservable();
  }

  setPayHistoryDetails(data: PaymentHistory) {
    this.PaymentHistorySubject.next(data);
  }
  
  getPayHistoryDetails(): Observable<PaymentHistory> {
    return this.PaymentHistorySubject.asObservable();
  }

  setClient(data: Client) {
    this.clientSubject.next(data);
  }
  
  getClient(): Observable<Client> {
    return this.clientSubject.asObservable();
  }

  setAppUser(data: AppUser) {
    this.appUserSubject.next(data);
  }
  
  getAppUser(): Observable<AppUser> {
    return this.appUserSubject.asObservable();
  }

  setUserType(data: string) {
    this.userTypeSubject.next(data);
  }
  
  getUserType(): Observable<string> {
    return this.userTypeSubject.asObservable();
  }

  // setJDAlign(data:any){
  // this.JDDataSubject = data;
  // }

  // getJDAlign(): Observable<string> {
  //   return this.JDDataSubject;
  // }


}
