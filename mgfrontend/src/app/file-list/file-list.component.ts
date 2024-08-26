import { Component } from '@angular/core';
import { FileService } from 'app/core/file.service';
import { Subscription } from "rxjs";
import { MessageService } from "primeng/api";
import { XcvUtilsService } from 'app/core/xcv-utils.service';

@Component({
  selector: 'app-file-list',
  templateUrl: './file-list.component.html',
  styleUrls: ['./file-list.component.scss']
})
export class FileListComponent {
  public selectedFiles: any;
  public fileList: any;
  public isLoadingData: boolean = false;
  public bucket_name = 'morguard-test-bucket';
  public isLoading: boolean = false;
  private subscription!: Subscription;
  public fileData: any;
  public fileDataList: any = [];
  public showfileDetails:boolean = false;
  public filetoprocess:any;
 
  constructor(
    private fileservice: FileService,
    private messageService: MessageService
  ) {}

  ngOnInit(): void {
    this.listAllDrives();
  }

  public listAllDrives(): void {
    this.isLoading = true;
    this.subscription = this.fileservice.listdrives(this.bucket_name).subscribe({
      next: (response: any) => {
        this.fileList = response['S3 folders'].map((item: any, index: number) => {
          // return {id:item.split('-')[0].trim(),name:item.split('-').slice(1).join(' ')}
          this.isLoading = false;
          return { id: index, name: item, label: item }
        });

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

public getAllfiles()  
{
  this.subscription = this.fileservice.expanddrive(this.bucket_name, this.selectedFiles.name).subscribe({
    next: (response: any) => {
      this.fileDataList = response
      console.log("this.fileDataList", this.fileDataList)
 
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

processFile(file:any)
{
this.filetoprocess = file;
}

getFileDetails(file:any) {

  this.isLoadingData = true;
  this.subscription = this.fileservice
    .getFileDetails(file, this.bucket_name, this.selectedFiles.name)
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

}
