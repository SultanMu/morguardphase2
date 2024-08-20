import { DatePipe } from '@angular/common';
import { Injectable } from '@angular/core';
import { Constants } from "app/helpers/app-settings";
import { ProfileEducation, ProfileExperience, ProfileProject, ProfilePublication } from "app/model/Userprofile";
import { MessageService } from 'primeng/api';

export class XcvUtilsService {

    constructor(
       ) {
    }

    public static handleError(error: any, messageService: MessageService, customMessage?: string) {
      if (customMessage) {
        messageService.add({ severity: 'error', summary: 'Error', detail: `${customMessage}`, life: 5000});
      } else {
        if (error.error && error.error.exception) {
          messageService.add({ severity: 'error', summary: 'Error', detail: `${error.error.exception}`, life: 5000});
        } else if (error.error && error.error.info) {
          messageService.add({ severity: 'error', summary: 'Error', detail: `${error.error.info}`, life: 5000});
        } else {
          messageService.add({ severity: 'error', summary: 'Error', detail: `${Constants.GENERIC_ERROR_MSG}`, life: 5000});
        }
      }
    }

    public static isNotNullOrEmpty(value: any): boolean {
        if (typeof value === 'string') {
          return value !== undefined && value !== null && value !== '';
        } else if (typeof value === 'number' || Object.prototype.toString.call(value) === '[object Date]'
          || Object.prototype.toString.call(value) === '[object File]') {
          return value !== undefined && value !== null;
        }
        return value !== undefined && value !== null && Object.keys(value).length !== 0;
      } 
         
    public static isNotEmpty(array: any[]): boolean {
        return this.isNotNullOrEmpty(array) && array.length > 0;
      }
        
    public static getPlanType(amount: number): string {
      if (amount === 14.99 || 
        amount === 1499 ||
        amount === 4.99 ||
        amount === 499) {
          return Constants.STANDARD;
      } else if (
        amount === 49.99 || 
        amount === 4999 ||
        amount === 149 ||
        amount === 14900
      ) {
        return Constants.PREMIUM;
      }
      return Constants.FREE;
    }   

    public static convertRealDateFormat(day: number, month: number, year: number): any {
      const date = new Date(year, month - 1, day);
      return date;
    }

    public static convertDateFormat(day: number, month: number, year: number, datePipe: DatePipe): any {
      const date = new Date(year, month - 1, day);
      return datePipe.transform(date, 'MMM d, y'); //    
    }

    public static sortPublications(publications: ProfilePublication[], sort: string): void {
      let sortedPublications: ProfilePublication[] = [];
      if (XcvUtilsService.isNotEmpty(publications)) {
        publications.forEach((pub: ProfilePublication) => {
          pub.published_on_date = this.convertRealDateFormat(pub.published_on?.day, pub.published_on?.month, pub.published_on?.year);
        });

        // then sort
        publications.sort(  (a, b) => {
          if (a.published_on_date === null && b.published_on_date === null) {
            return 0; // If both are null, leave them as is
          } else if (a.published_on_date === null) {
            return 1; // Put items with no date at the bottom
          } else if (b.published_on_date === null) {
            return -1; // Put items with no date at the bottom
          } else {
            // Sort by date in descending order
            if (b.published_on_date && a.published_on_date) {
              // return b.published_on_date.getTime() - a.published_on_date.getTime();

              if (sort === Constants.ASC) {
                return a.published_on_date.getTime() - b.published_on_date.getTime();
              } else {
                return b.published_on_date.getTime() - a.published_on_date.getTime();
              }
            } else {
              return 0;
            }
          }
        });


      }
    }

    public static sortProject(project: ProfileProject[]) {
      if (project) {
        project.forEach((ex: ProfileProject) => {

              if (ex.starts_at?.day && ex.starts_at?.month && ex.starts_at?.year) {
                  ex.starts_date = this.convertRealDateFormat(ex.starts_at?.day, ex.starts_at?.month, ex.starts_at?.year);
              } else {
                  delete ex.starts_date;
              }
          });

          return project.slice().sort(this.compareDatesDesc);
      } else {
          return [];
      }
    }    

    public static sortEducation(education: ProfileEducation[]) {
      if (education) {
          education.forEach((ex: ProfileEducation) => {

              if (ex.starts_at?.day && ex.starts_at?.month && ex.starts_at?.year) {
                  ex.starts_date = this.convertRealDateFormat(ex.starts_at?.day, ex.starts_at?.month, ex.starts_at?.year);
              } else {
                  delete ex.starts_date;
              }
          });

          return education.slice().sort(this.compareDatesDesc);
      } else {
          return [];
      }
    }    

    public static compareDatesDesc(a: any, b: any) {
      if (a.starts_date === undefined && b.starts_date === undefined) {
        return 0;
      }
  
      if (a.starts_date === undefined) {
        return 1; // Place null dates at the bottom
      }
  
      if (b.starts_date === undefined) {
        return -1; // Place null dates at the bottom
      }
  
      // Compare dates in descending order
      return b.starts_date.getTime() - a.starts_date.getTime();
    }

    public static sortExperience(experience: ProfileExperience[], sort: string): void {
      let sortedExperience: ProfileExperience[] = [];

      if (XcvUtilsService.isNotEmpty(experience)) {

        // create the actual javascript date object
        experience.forEach((ex: ProfileExperience) => {
          ex.starts_date = this.convertRealDateFormat(ex.starts_at?.day, ex.starts_at?.month, ex.starts_at?.year);
          if (ex.ends_at?.day && ex.ends_at?.month && ex.ends_at?.year) {
              ex.ends_date = this.convertRealDateFormat(ex.ends_at?.day, ex.ends_at?.month, ex.ends_at?.year);
          }
        });

        // then sort
        experience.sort(  (a, b) => {
          if (a.starts_date === null && b.starts_date === null) {
            return 0; // If both are null, leave them as is
          } else if (a.starts_date === null) {
            return 1; // Put items with no date at the bottom
          } else if (b.starts_date === null) {
            return -1; // Put items with no date at the bottom
          } else {
            // Sort by date in descending order
            if (b.starts_date && a.starts_date) {
              // return b.starts_date.getTime() - a.starts_date.getTime();

              if (sort === Constants.ASC) {
                return a.starts_date.getTime() - b.starts_date.getTime();
              } else {
                return b.starts_date.getTime() - a.starts_date.getTime();
              }
            } else {
              return 0;
            }
          }
        });
      }
    }

}