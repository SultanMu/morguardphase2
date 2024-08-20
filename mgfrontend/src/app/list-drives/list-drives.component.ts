import { Component, HostListener, } from '@angular/core';

import { FormBuilder } from "@angular/forms";
import { LocalStorageService } from "app/core/local-storage.service";
import { DataService } from "app/helpers/data.service";
import { Subscription } from "rxjs";
import { MessageService } from "primeng/api";
import { AppUser, Client } from "app/model/Userprofile";
import { AytHttpParams } from "app/helpers/http-config";
import { Constants } from "app/helpers/app-settings";
import { FileService } from "app/core/file.service";
import { XcvUtilsService } from 'app/core/xcv-utils.service';
interface DropdownItem {
  label: string;
  value: string;
}

interface DropdownGroup {
  label: string;
  items: DropdownItem[];
}
@Component({
  selector: 'app-list-drives',
  templateUrl: './list-drives.component.html',
  styleUrls: ['./list-drives.component.scss']
})
export class ListDrivesComponent {
  public selectedFiles: any;
  // public fileList: any = [
  //   { id: 1, name: "File 01" },
  //   { id: 2, name: "File 02" },
  //   { id: 3, name: "File 03" },
  //   { id: 4, name: "File 04" },
  //   { id: 5, name: "File 05" },
  // ];
  public fileList: any;
  public mappedfiles: any;
  public displayDialog: boolean = false;
  public isSmallScreen = false;
  public first_name = "";
  private subscription!: Subscription;
  public appUser: AppUser = {};
  public client: Client = new Client();
  public userType = Constants.CLIENT;
  public isLoading: boolean = false;
  public isLoadingData: boolean = false;
  jwt: any;
  uuid: any;
  fileData: any;
  fileDataList: any = [];
  isExpanded = false;
  selectedFileGroup:any;
  public mappedList : DropdownGroup[] = [];
  

  public bucket_name = 'morguard-test-bucket';
  constructor(
    private fb: FormBuilder,
    private dataService: DataService,
    private localStorageService: LocalStorageService,
    private fileservice: FileService,
    private messageService: MessageService
  ) {}

  @HostListener("window:resize", ["$event"])  
  onResize(event: Event) {
    this.checkScreenSize();
  }

  private checkScreenSize() {
    const isSmallScreen = window.innerWidth <= 767; // Match the CSS media query width
    this.isSmallScreen = isSmallScreen;
    // You can also dynamically apply a CSS class if needed
    if (isSmallScreen) {
      this.displayDialog = false;
    } else {
      this.displayDialog = true;
    }
  }
  ngAfterViewInit() {
    setTimeout(() => {
      this.dataService.setData("true");
      this.dataService.setName(this.first_name);
      this.dataService.setVanity("");
      this.dataService.setClient(this.client);
      this.dataService.setUserType(this.userType);
    }, 500);
  }
  ngOnInit(): void {
    this.appUser = this.localStorageService.getData('appUser');
    this.checkScreenSize();
    // get user from storage
    this.appUser = this.localStorageService.getData("appUser");
    if (this.appUser) {
      this.dataService.setAppUser(this.appUser);
    }
    this.listAllDrives();
  }


  public listAllDrives(): void {
    this.isLoading = true;
    const jwtToken = this.getCookie('jwt');
    this.subscription = this.fileservice.listdrives(this.bucket_name).subscribe({
      next: (response: any) => {
        this.fileList = response['S3 folders'].map((item: any, index: number) => {
          // return {id:item.split('-')[0].trim(),name:item.split('-').slice(1).join(' ')}
          this.isLoading = false;
          return { id: index, name: item, label: item }
        });
        this.fileList.forEach((fileslist: any) => {
        this.getSamplefiles(fileslist.name)
})
      },
      error: (error: any) => {
        this.messageService.add({
          severity: "warn",
          summary: "Warn",
          detail: "Something went wrong",
          life: 5000,
        });
      },
    });
    console.log("this.fileDataList", this.fileDataList)
  }
  public getSamplefiles(filename: any): void {
    const jwtToken = this.getCookie('jwt');
    this.subscription = this.fileservice.expanddrive(this.bucket_name, filename).subscribe({
      next: (response: any) => {
        response.label = filename;
        this.fileDataList.push(response)
        this.mappedList = this.fileDataList.map((group: any) => ({
          label: group.label,
          items: group.files.map((item: any) => ({ label: item, value: item }))
        }));
      },
      error: (error: any) => {
        this.messageService.add({
          severity: "warn",
          summary: "Warn",
          detail: "Something went wrong",
          life: 5000,
        });
      },
    });
  }
  public getCookie(name: string): string | null {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
      return parts.pop()?.split(';').shift() || null;
    }
    return null;
  }
  onFileChange(event:any)
  {
    const selectedItem = event.value;
    const parentGroup = this.mappedList.find(group => 
      group.items.some(item => item.value === selectedItem)
    );
    if (parentGroup) {
     this.selectedFileGroup = parentGroup.label;
    }
  }

  getFileDetails() {
    this.isLoadingData = true;
    this.subscription = this.fileservice
      .getFileDetails(this.selectedFiles, this.bucket_name, this.selectedFileGroup)
      .subscribe({
        next: (response: any) => {
          this.isLoadingData = false;
          if(response){
            const filejsonObject = response[0][this.selectedFiles];
            this.fileData = this.removeSpacesWithinKeys(filejsonObject);
            console.log(this.fileData)
          }
        
        },
        error: (error: any) => {
          console.log('error',error)
          XcvUtilsService.handleError(error, this.messageService);
          this.isLoading = false;
        },
      });
  }

  public removeSpacesWithinKeys(obj: any): any {
    const newObj: any = {};
    Object.keys(obj).forEach(key => {
      const newKey = key.replace(/\s+/g, ''); // Remove spaces within key
      if (typeof obj[key] === 'object' && obj[key] !== null) {
        newObj[newKey] = this.removeSpacesWithinKeys(obj[key]);
      } else {
        newObj[newKey] = obj[key];
      }
    });
    return newObj;
  }
  
  ngOnDestroy(): void {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
}
