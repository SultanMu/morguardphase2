import { AfterViewInit, Component, HostListener, OnDestroy, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { MessageService } from 'primeng/api';
import { LocalStorageService } from 'app/core/local-storage.service';
import { HttpClient } from '@angular/common/http';
import { UserService } from 'app/core/user.service';
import { DataService } from 'app/helpers/data.service';
import { SharedService } from 'app/core/shared.service';
import { EmailValidator } from 'app/helpers/xcv-validator';
import { XcvUtilsService } from 'app/core/xcv-utils.service';
import * as EmailValidatorFake from 'email-validator';
@Component({
  selector: 'app-company-register',
  templateUrl: './company-register.component.html',
  styleUrls: ['./company-register.component.scss']
})
export class CompanyRegisterComponent implements AfterViewInit, OnInit, OnDestroy {
  public displayDialog: boolean = false;
  public isSmallScreen = false;
  public registerCompanyForm!: FormGroup;
  public submitted = false;
  public processing = false;

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
      this.createRegisterForm();
      // this part takes care of checking password and confirm password
      this.registerCompanyForm.controls['password1'].valueChanges.subscribe(() => this.validatePasswordMatch());
      this.registerCompanyForm.controls['password2'].valueChanges.subscribe(() => this.validatePasswordMatch());
      this.registerCompanyForm.controls['companyEmail'].valueChanges.subscribe(() => this.validateEmail());
  }

  @HostListener('window:resize', ['$event'])
  onResize(event: Event) {
    this.checkScreenSize();
  }

  private createRegisterForm() {
    this.registerCompanyForm = this.fb.group({
      companyName: ['',[Validators.required]],
      companyEmail: ['', [Validators.required, EmailValidator()]],
      password1: ['', [Validators.required,this.validatePassword]],
      password2: ['', [Validators.required]],
      
    });
  }
  validatePassword(control: any) {
    const password = control.value;
    if (!password) {
      return null;
    }
    else {
      const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#^])[A-Za-z\d@$!%*?&#^]{8,}$/;

      return passwordPattern.test(control.value) ? null : { 'weakPassword': true };
    }
    // Minimum eight characters, at least one uppercase letter, one lowercase letter, one number, and one special character
  }
  ngOnInit(): void {
    this.checkScreenSize();
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
  

  public onSubmit() {
    this.submitted = true;
    if (this.registerCompanyForm.valid) {
      this.executeRegisterCompany();
    }
  }

  public resetCompanyForm() {
    this.submitted = false;
    this.registerCompanyForm.setErrors(null);
    this.registerCompanyForm.reset();
  }

  public executeRegisterCompany() {
    // TODO place the API call here to register the company when backend API is ready
    console.log("register called")
    let payload: any = {};
    payload.name =  this.registerCompanyForm.controls['companyName'].value;
    payload.email =  this.registerCompanyForm.controls['companyEmail'].value;
    payload.password =  this.registerCompanyForm.controls['password1'].value;
    this.processing = true;
    console.log('>>>> payload = ', payload);
    this.subscription = this.userService.registerUser(payload).subscribe({
      next: response => {
        if (response) {
          this.processing = false;
          this.messageService.add({ severity: 'success', summary: 'Success', detail: `User registered successfully`, life: 5000});
          this.submitted = false;
          // clear the form
          this.resetCompanyForm();
          // go to login
          
          this.router.navigate(['/login'])
        }
      },
      error: error => {
        this.processing = false;
        this.submitted = false;
        XcvUtilsService.handleError(error, this.messageService);
      }
    });
  }


  public validatePasswordMatch() {
    const password = this.registerCompanyForm.controls['password1'].value;
    const confirmPassword = this.registerCompanyForm.controls['password2'].value;

    if (confirmPassword) {
      if (password === confirmPassword) {
        this.registerCompanyForm.controls['password2'].setErrors(null);
      } else {
        this.registerCompanyForm.controls['password2'].setErrors({ passwordMismatch: true });
      }
    } else {
      this.registerCompanyForm.controls['password2'].setErrors({ required: true });
    }
  }
    
  public validateEmail(){
    const email = this.registerCompanyForm.controls['companyEmail'].value;
    let isEmailValid = EmailValidatorFake.validate(email); 
    if(!isEmailValid)
      {
        this.registerCompanyForm.controls['companyEmail'].setErrors({ emailInvalid: true });
      }
  }  
  public recruiterLogin(): void {
    this.router.navigate(['/login']);
    // this.router.navigate(['payment'],{ queryParams: {'optionType': 'premium', 'origin': 'recruiter'}})
  }
  public clientLogin() {
    // this.rerouteTasks();
    this.router.navigate(['/login'])
  }

  ngOnDestroy(): void {
    if (this.subscription) {
      this.subscription.unsubscribe;
    }
  }  

}
