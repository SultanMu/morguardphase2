import { Injectable } from '@angular/core';
import { LocalStorageService } from '../core/local-storage.service';
import { AppUser, Client, SubscriptionPlan } from '../model/Userprofile';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private isLoggedIn = false;

  constructor(
    private localStorageService: LocalStorageService
  ) { }

  login(appUser: AppUser) {
    // Implement your login logic here
    this.isLoggedIn = true;
    this.localStorageService.saveData('appUser', appUser);
  }

  logout() {
    // Implement your logout logic here
    this.isLoggedIn = false;
    this.localStorageService.removeData('appUser');
  }

  isLoggedInUser(): boolean {
    let isIn = false;
    let appUser = this.localStorageService.getData('appUser');
    if (appUser) {
      isIn = true;
    }
    // return this.isLoggedIn || isIn;
    return isIn;
  }

}
