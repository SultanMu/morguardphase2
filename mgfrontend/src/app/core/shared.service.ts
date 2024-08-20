import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  private userId : any;

  constructor() { }
  set userToEdit(userId) {
    this.userId = userId;
  }

  get userToEdit() {
    return this.userId;
  }
}
