import { HttpClient } from '@angular/common/http';
import { AfterViewInit, Component, HostListener, OnDestroy, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, ValidatorFn, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { LocalStorageService } from 'app/core/local-storage.service';
import { SharedService } from 'app/core/shared.service';
import { UserService } from 'app/core/user.service';
import { XcvUtilsService } from 'app/core/xcv-utils.service';
import { DataService } from 'app/helpers/data.service';
import { EmailValidator } from 'app/helpers/xcv-validator';
import { MessageService } from 'primeng/api';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.scss']
})


export class ResetPasswordComponent implements AfterViewInit, OnInit, OnDestroy {

  public token = '';
  public hasToken = true;
  public resetForm!: FormGroup;
  public processing = false;
  public isSmallScreen = false;
  public displayDialog: boolean = false;
  public submitted!: boolean;
  public countdown: number = 6; // Initial countdown value
  public redirectMessage: string = 'Token and Email is required';
  public email = '';
  public hasEmail = true;
  public isValid = true;

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
      this.createResetForm();
      // this part takes care of checking password and confirm password
      this.resetForm.controls['password1'].valueChanges.subscribe(() => this.validatePasswordMatch());
      this.resetForm.controls['password2'].valueChanges.subscribe(() => this.validatePasswordMatch());
    }

    @HostListener('window:resize', ['$event'])
    onResize(event: Event) {
      this.checkScreenSize();
    }

    ngOnInit(): void {
      this.checkScreenSize();
      this.subscribeToQueryParams();
    }

    private createResetForm() {
      this.resetForm = this.fb.group({
        password1: ['', [Validators.required]],
        password2: ['', [Validators.required]],
      });
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

    private subscribeToQueryParams() {
      this.subscription = this.activatedRoute.queryParams.subscribe((queryParams: any) => {
        if (queryParams.hasOwnProperty('token') && queryParams.token !== '') {
          this.token = queryParams.token;
          this.hasToken = true;
          // do you thing
        } else {
          this.hasToken = false;
          this.isValid = false;
          // this.startCountdown();
        }

        if (queryParams.hasOwnProperty('email') && queryParams.email !== '') {
          this.email = queryParams.email;
          // do you thing
        } else {
          this.hasEmail = false;
          this.isValid = false;
          // this.startCountdown();
        }

        if (!this.isValid) {
          this.startCountdown();
        }


      });
      
    }

    ngAfterViewInit(): void {
      setTimeout(() => {
        this.dataService.setData('false');
      }, 10);
    }
  
    startCountdown(): void {
      const countdownInterval = setInterval(() => {
        this.countdown--;
        if (this.countdown <= 0) {
          clearInterval(countdownInterval);
          this.redirectToLogin();
        }
      }, 1000);
    }
      
    redirectToLogin() {
      this.router.navigate(['/login']);
    }

    public onSubmit(): void {
      this.submitted = true;
      if (this.resetForm.valid) {
        const { password1, password2 } = this.resetForm.value;
        if (password1 === password2) {

          let payload: any = {};
          payload.email = this.email;
          payload.password1 = password1;
          payload.password2 = password2;
          payload.token =  this.token;

          this.processing = true;

          this.subscription = this.userService.passwordUpdateRecruiter(payload).subscribe({
            next: response => {
              this.processing = false;
              this.messageService.add({ severity: 'success', summary: 'Success', detail: `Password successfully updated`, life: 5000});

              // redirect to recruiter login
              this.router.navigate(['/recruiter-login']);
            },
            error: error => {
              XcvUtilsService.handleError(error, this.messageService);
              this.processing = false;
            }
          });
        } else {
          this.messageService.add({ severity: 'warn', summary: 'Warn', detail: `Passwords do not match`, life: 5000});
        }
      }
    }

    public validatePasswordMatch() {
      const password = this.resetForm.controls['password1'].value;
      const confirmPassword = this.resetForm.controls['password2'].value;
  
      if (confirmPassword) {
        if (password === confirmPassword) {
          this.resetForm.controls['password2'].setErrors(null);
        } else {
          this.resetForm.controls['password2'].setErrors({ passwordMismatch: true });
        }
      } else {
        this.resetForm.controls['password2'].setErrors({ required: true });
      }
    }    

    private rerouteTasks(): void {
      // remove from storage.
      this.localStorageService.removeData('userVanity');
      this.localStorageService.removeData('userClient');
      this.localStorageService.removeData('subcriptionPlan');
      this.localStorageService.removeData('appUser');
    }
  
    public clientLogin() {
      this.rerouteTasks();
      this.router.navigate(['login'])
    }

    public recruiterLogin(): void {
      this.router.navigate(['/recruiter-login']);
    }
  
    ngOnDestroy(): void {
    }
  
}
