import { HttpClient, HttpHeaders } from '@angular/common/http';
import { AfterViewInit, Component, HostListener, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { SharedService } from '../core/shared.service';
import { Subscription } from 'rxjs';
import { UserService } from '../core/user.service';
import { DataService } from 'app/helpers/data.service';
import { LocalStorageService } from 'app/core/local-storage.service';
import { MessageService } from 'primeng/api';
import { AppUser } from 'app/model/Userprofile';
import { XcvUtilsService } from 'app/core/xcv-utils.service';
import { EmailValidator } from 'app/helpers/xcv-validator';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements AfterViewInit, OnInit {
  public processing = false;
  public submitted = false;
  public displayDialog: boolean = false;
  public isSmallScreen = false;
  public loginForm!: FormGroup;
  private subscription!: Subscription;
  // public privacyModal = false;

  visible: boolean = false;

    showDialog() {
        this.visible = true;
    }

  // linkedInCredentials = {
  //   clientId: "86lukxm5jr2z3u",
  //   redirectUrl: "/login",
  //   scope: "r_liteprofile%20r_emailaddress%20w_member_social" // To read basic user profile data and email
  // };


  constructor(private fb: FormBuilder,
    private router:Router,
    private messageService: MessageService,    
    private localStorageService: LocalStorageService,
    private http:HttpClient,
    private userService: UserService,
    private activatedRoute: ActivatedRoute,    
    private dataService: DataService,
    private sharedService: SharedService) {}

  @HostListener('window:resize', ['$event'])
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

  ngOnInit(): void {
    this.checkScreenSize();
    this.createLoginForm();
  }
  ngAfterViewInit() {
    setTimeout(() => {
      this.dataService.setData('false');
    }, 10);
  }

  private createLoginForm() {
    this.loginForm = this.fb.group({
      username: ['',[Validators.required, EmailValidator()]],
      password: ['', Validators.required],
      rememberMe: [false], // Checkbox for "Remember Me"
    });
  }
  public onSubmit() {
    this.submitted = true;

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
            // data.token = response.jwt;
            this.localStorageService.saveData('appUser', data);
            // document.cookie = `jwt=${cookieValue}; expires=...; path=/`;
            document.cookie = `jwt=${cookieValue}; path=/`;
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

  }

  public recruiterLogin(): void {
    this.router.navigate(['/recruiter-login']);
  }

  public register(): void {
    this.router.navigate(['company-register']);
    // this.router.navigate(['payment'],{ queryParams: {'optionType': 'premium', 'origin': 'recruiter'}})
  }

}
