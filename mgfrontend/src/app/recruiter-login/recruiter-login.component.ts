import { HttpClient } from '@angular/common/http';
import { AfterViewInit, Component, HostListener, OnDestroy, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { LocalStorageService } from 'app/core/local-storage.service';
import { SharedService } from 'app/core/shared.service';
import { UserService } from 'app/core/user.service';
import { DataService } from 'app/helpers/data.service';
import { AytHttpParams } from 'app/helpers/http-config';
import { MessageService } from 'primeng/api';
import { Subscription } from 'rxjs';
import { EmailValidator } from 'app/helpers/xcv-validator';
import { AppUser } from 'app/model/Userprofile';
import { Constants } from 'app/helpers/app-settings';
import { XcvUtilsService } from 'app/core/xcv-utils.service';

@Component({
  selector: 'app-recruiter-login',
  templateUrl: './recruiter-login.component.html',
  styleUrls: ['./recruiter-login.component.scss']
})
export class RecruiterLoginComponent implements AfterViewInit, OnInit, OnDestroy {

  public displayDialog: boolean = false;
  public isSmallScreen = false;
  public loginForm!: FormGroup;
  public companyLoginForm!: FormGroup;
  public forgotForm!: FormGroup;
  public processing = false;
  public processingCompany = false;
  public submitted = false;
  public submittedCompany = false;

  public forgotPasswordMode = false;
  public forgotPasswordType: string = Constants.RECRUITER; // this will be passed to determine if forgot password is for company or recruiter

  private subscription!: Subscription;

  constructor(private fb: FormBuilder,
    private router:Router,
    private messageService: MessageService,    
    private localStorageService: LocalStorageService,
    private http: HttpClient,
    private userService: UserService,
    private activatedRoute: ActivatedRoute,    
    private dataService: DataService,
    private sharedService: SharedService) {
      this.createLoginForm();
      this.createForgotpasswordForm();
    }

    @HostListener('window:resize', ['$event'])
    onResize(event: Event) {
      this.checkScreenSize();
    }
  
  ngOnInit(): void {
    this.createLoginForm();
    //check local storage for rememberMe
    let ls: any = this.localStorageService.getData('rememberMe');
    this.localStorageService.removeData('subcriptionType');
    if (ls) {
      this.loginForm.controls['username'].setValue(ls.username);
      this.loginForm.controls['rememberMe'].setValue(true);
    }
    this.checkScreenSize();
  }

  public toggleForgotPasswordMode(): void {
    
    this.forgotPasswordMode = true;
  }

  private createLoginForm() {
    this.loginForm = this.fb.group({
      username: ['',[Validators.required, EmailValidator()]],
      password: ['', Validators.required],
      rememberMe: [false], // Checkbox for "Remember Me"
    });
  }
  private executeForgotPassword(): void {
    if (this.forgotForm.valid) {
      const {email} = this.forgotForm.value;
      let p = new AytHttpParams();
      p.set('email', email);
      p.set('type', this.forgotPasswordType);

      this.processing = true;
      this.subscription = this.userService.passwordResetRecruiter(p).subscribe({
        next: response => {
          this.processing = false;

          // reset form
          this.forgotFormReset();
          this.messageService.add({ severity: 'success', summary: 'Success', detail: `Email to reset password successfully sent`, life: 5000});

          this.forgotPasswordMode = false;
        },
        error: error => {
          XcvUtilsService.handleError(error, this.messageService);
          this.processing = false;
        }
      });
    }
  }
  private createForgotpasswordForm() {
    this.forgotForm = this.fb.group({
      email: ['',[Validators.required, EmailValidator()]]
    });
  }

  public onSubmit() {
    this.submitted = true;
    if (!this.forgotPasswordMode) {
      if (this.loginForm.valid) {
        const { username, password, rememberMe } = this.loginForm.value;
        let payload: any = {};
        payload.email =  username;
        payload.password =  password;
        this.processing = true;
        this.subscription = this.userService.loginUser(payload).subscribe({
          next: response => {
            this.processing = false;

            // save to local stoage
            if (rememberMe) {
              const data = { username: username, checkbox: true};
              this.localStorageService.saveData('rememberMe', data);
            } else {
              this.localStorageService.removeData('rememberMe');             
            }
            console.log('>>>> recruiter = ', response);
            // save creds on local storage
            // const data: AppUser = { first_name: username};
            const data: AppUser = {};
            const cookieValue = response.jwt;
            data.email = username;
            data.token = response.jwt;
            this.localStorageService.saveData('appUser', data);
            document.cookie = `jwt=${cookieValue}; expires=...; path=/`;
            // set on the header
            this.dataService.setAppUser(data);
            this.router.navigate(['/list-drives']);
          },
          error: error => {
            XcvUtilsService.handleError(error, this.messageService);
            this.processing = false;
          }
        });
      }
  
    } else {
      // forgot password
      this.executeForgotPassword();
    }
  }

  ngAfterViewInit(): void {
    setTimeout(() => {
      this.dataService.setData('false');
    }, 10);
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

  public mainLogin(): void {
    this.router.navigate(['/login']);
  }

  public forgotFormReset(): void {
    this.submitted = false;
    this.createForgotpasswordForm();
  }

  public back(): void {
    this.forgotPasswordMode = false;
    this.forgotFormReset();
  }

  public register(): void {
    this.router.navigate(['company-register']);
    // this.router.navigate(['payment'],{ queryParams: {'optionType': 'premium', 'origin': 'recruiter'}})
  }

  private rerouteTasks(): void {
    // remove from storage.
    this.localStorageService.removeData('appUser');
  }

  public clientLogin() {
    this.rerouteTasks();
    this.router.navigate(['login'])
  }


  ngOnDestroy(): void {
    if (this.subscription) {
      this.subscription.unsubscribe;
    }
  }  

}
