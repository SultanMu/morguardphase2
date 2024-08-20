import { Component, OnDestroy, OnInit, AfterViewInit } from "@angular/core";
import { LocalStorageService } from "./core/local-storage.service";
import { DataService } from "./helpers/data.service";
import { Subscription } from "rxjs";
import { MenuItem, MessageService } from "primeng/api";
import { Router } from "@angular/router";
import {
  AppUser,
  Client,
  PaymentHistory,
  SubscriptionDetails,
  SubscriptionPlan,
  subcriptionType,
} from "./model/Userprofile";
import { Constants } from "./helpers/app-settings";
import { UserService } from "./core/user.service";
import { XcvUtilsService } from "./core/xcv-utils.service";
import { AytHttpParams } from "./helpers/http-config";
import { createPopper } from "@popperjs/core";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"],
  providers: [MessageService],
})
export class AppComponent implements OnInit, AfterViewInit, OnDestroy {
  title = "xCV-demo";
  isLoggedIn = false;
  name = "";
  vanity_name = "";
  userType = Constants.CLIENT;
  initials = "";
  subscriptionPlan: SubscriptionPlan = {};
  client: Client = new Client();
  appUser: AppUser = {};
  subscription: Subscription;
  items: MenuItem[] | undefined;
  subcriptionType: subcriptionType = {};
  email!: any;
  message = "";
  subject = "";
  isOpenSupportModel = false;
  isNavbarExpanded = false;
  subscriptionDetails: SubscriptionDetails = {};
  payHistoryDetails: PaymentHistory = {};
  public trialLimit: any;
  public showStatusdetails = false;
  public noOfLicenses: any;
  navbarCollapsed = true;

  constructor(
    private localStorageService: LocalStorageService,
    private router: Router,
    private userService: UserService,
    private messageService: MessageService,
    private dataService: DataService
  ) {
    this.subscription = this.dataService.getData().subscribe((data) => {
      this.isLoggedIn = /true/i.test(data);
    });

    this.subscription = this.dataService.getName().subscribe((data) => {
      // this.name = data;
      if (this.name) {
        const names = this.name.split(" ");
        const initials = names.map((n) => n[0]).join("");
        this.initials = initials.toUpperCase();
      }
    });

    this.subscription = this.dataService.getUserType().subscribe((data) => {
      this.userType = data;
    });

    this.subscription = this.dataService.getVanity().subscribe((data) => {
      this.vanity_name = data;
    });

    this.subscription = this.dataService
      .getSubscriptionPlan()
      .subscribe((data) => {
        this.subscriptionPlan = data;
      });

    this.subscription = this.dataService
      .getSubscriptionDetails()
      .subscribe((data) => {
        this.subscriptionDetails = data;
      });

    this.subscription = this.dataService
      .getPayHistoryDetails()
      .subscribe((data) => {
        this.payHistoryDetails = data;
      });

    this.subscription = this.dataService.getClient().subscribe((data) => {
      this.client = data;
      this.isClientValid();
    });

    this.subscription = this.dataService.getAppUser().subscribe((data) => {
      this.appUser = data;

      this.showPricing();

      if (this.name) {
        const names = this.name.split(" ");
        const initials = names.map((n) => n[0]).join("");
        this.initials = initials.toUpperCase();
      }
    });
  }

  toggleNavbarCollapsing() {
    this.navbarCollapsed = !this.navbarCollapsed;
  }

  openSupportModal(): void {
    let company = this.localStorageService.getData("appUser");
    if (company) {
      this.email = company.email;
      this.message = "";
      this.subject = "";
    }
  }

  logFormData(): void {
    let company = this.localStorageService.getData("appUser");

    if (!this.subject) {
      this.messageService.add({
        severity: "error",
        summary: "Error",
        detail: `Subject field is requied`,
        life: 5000,
      });
      return;
    }
    if (!company.email && !this.email) {
      this.messageService.add({
        severity: "error",
        summary: "Error",
        detail: `Email field is requied`,
        life: 5000,
      });
      return;
    }
    if (company.user_type !== "CLIENT") {
      this.sendSupportMessage(
        company.email,
        company.company_name,
        this.message,
        this.subject
      );
    } else {
      this.sendSupportMessage(
        this.email,
        company.company_name,
        this.message,
        this.subject
      );
    }
    this.email = company.email ? company.email : "";
    this.message = "";
    this.subject = "";
  }
  ngOnInit(): void {
    this.constructMenu();
    let company = this.localStorageService.getData("appUser");
    this.payHistoryDetails = this.localStorageService.getData("paymentHistory");
    this.subscriptionDetails =
      this.localStorageService.getData("subcriptionType");
    if (company) {
      this.email = company.email;
    }
    if (this.subscriptionDetails) {
      if (
        this.subscriptionDetails.status === "active" ||
        this.subscriptionDetails.status === "canceled" ||
        this.subscriptionDetails.status === "trialing"
      ) {
        this.showStatusdetails = true;
      }
    }

    // if (company && company.email) {
    //   // this.getSubscriptionDetails(company.email)
    //   setTimeout(() => {
    //     // this.calcPlan(this.payHistoryDetails);
    //     this.getTrialLimit(this.subscriptionDetails);
    //   }, 1000);
    // }
  }

  ngAfterViewInit() {
    setTimeout(() => {
      this.subscriptionDetails =
        this.localStorageService.getData("subcriptionType");
      if (this.subscriptionDetails) {
        if (
          this.subscriptionDetails.status === "active" ||
          this.subscriptionDetails.status === "canceled" ||
          this.subscriptionDetails.status === "trialing"
        ) {
          this.showStatusdetails = true;
        }
      }
    }, 1000);
  }

  public sendSupportMessage(
    user_email: string,
    user_name: string,
    message: string,
    subject: string
  ): void {
    const payload = {
      ticketSubject: subject,
      ticketDescription: message,
      userEmail: user_email,
      userName: user_name,
    };

    this.subscription = this.userService.sendSupportMessage(payload).subscribe({
      next: (response) => {
        this.messageService.add({
          severity: "success",
          summary: "success",
          detail: `Message sent successfully`,
          life: 5000,
        });
      },
      error: (error) => {
        XcvUtilsService.handleError(error, this.messageService);
      },
    });
  }

  // public getSubscriptionDetails(company_email: any): void {
  //   let p = new AytHttpParams();
  //   p.set('company_email', company_email);
  //   this.subscription = this.userService.verifyPaymentPlan(p).subscribe({
  //     next: response => {
  //       this.subscriptionDetails = response;
  //       this.localStorageService.saveData('subcriptionType', response);
  //       this.subscriptionDetails = this.localStorageService.getData('subcriptionType');
  //       if (this.subscriptionDetails.status === 'trialing') {
  //         this.getTrialLimit(this.subscriptionDetails)
  //       }
  //     },
  //     error: error => {
  //       XcvUtilsService.handleError(error, this.messageService);
  //     }
  //   });
  // }

  // public getPaymenthistory(company_email: any): void {
  //   let p = new AytHttpParams();
  //   p.set('company_email', company_email);
  //   this.subscription = this.userService.getPaymentHistory(p).subscribe({
  //     next: response => {
  //       this.payHistoryDetails = response;
  //       this.calcPlan(response);
  //     },
  //     error: error => {
  //       XcvUtilsService.handleError(error, this.messageService);
  //     }
  //   });
  // }

  // public calcPlan(paydetails: any) {
  //   var previousPlan = paydetails.p_payment_type[paydetails.p_payment_type.length - 1];
  //   var planendDate = paydetails.p_valid_till[paydetails.p_valid_till.length - 1];
  //   var currentPlan = this.localStorageService.getData('subcriptionType');
  //   var validTill = new Date(planendDate)
  //   var todayDate = new Date();
  //   if (currentPlan && currentPlan.payment_type && paydetails.p_payment_type.length > 0 ) {

  //     if(currentPlan.status === 'active'){
  //       if(previousPlan === 'NA'){
  //         this.noOfLicenses = currentPlan.payment_type;
  //       }else{
  //         if (parseInt(previousPlan) > parseInt(currentPlan.payment_type)) {
  //           if (validTill > todayDate) {
  //             this.noOfLicenses = previousPlan;
  //           }
  //           else {
  //             this.noOfLicenses = currentPlan.payment_type;
  //           }
  //         }
  //         if (parseInt(previousPlan) <= parseInt(currentPlan.payment_type))
  //           {
  //           this.noOfLicenses = currentPlan.payment_type;
  //         }
  //       }

  //     }

  //     if(currentPlan.status === 'canceled'){

  //       if (validTill > todayDate) {
  //         this.noOfLicenses = previousPlan;
  //       }
  //     }
  //   }
  //   else {
  //     this.noOfLicenses = currentPlan.payment_type;
  //   }
  // }

  // public getTrialLimit(subsDetails: any): void {
  //   //var dateStr = "2024-03-30T12:00:00Z";
  //   const endDate = new Date(subsDetails.ends_at);
  //   // Get today's date
  //   const today = new Date();
  //   // Calculate the difference in milliseconds
  //   var difference = endDate.getTime() - today.getTime();
  //   // Convert milliseconds to days
  //   var daysDifference = Math.ceil(difference / (1000 * 60 * 60 * 24));
  //   //var daysDifference = Math.floor(difference / (1000 * 60 * 60 * 24));
  //   this.trialLimit = daysDifference;
  // }

  private constructMenu() {
    this.items = [
      {
        label: "Homes",
        icon: "pi pi-fw pi-home",
        command: (e) => this.reRouteToHome(),
        // items: [
        //     {
        //         label: 'New',
        //         icon: 'pi pi-fw pi-plus',
        //         items: [
        //             {
        //                 label: 'Bookmark',
        //                 icon: 'pi pi-fw pi-bookmark'
        //             },
        //             {
        //                 label: 'Video',
        //                 icon: 'pi pi-fw pi-video'
        //             }
        //         ]
        //     },
        //     {
        //         label: 'Delete',
        //         icon: 'pi pi-fw pi-trash'
        //     },
        //     {
        //         separator: true
        //     },
        //     {
        //         label: 'Export',
        //         icon: 'pi pi-fw pi-external-link'
        //     }
        // ]
      },
      {
        label: "Users",
        icon: "pi pi-fw pi-user",
        items: [
          {
            label: "New",
            icon: "pi pi-fw pi-user-plus",
          },
          {
            label: "Delete",
            icon: "pi pi-fw pi-user-minus",
          },
          {
            label: "Search",
            icon: "pi pi-fw pi-users",
            items: [
              {
                label: "Filter",
                icon: "pi pi-fw pi-filter",
                items: [
                  {
                    label: "Print",
                    icon: "pi pi-fw pi-print",
                  },
                ],
              },
              {
                icon: "pi pi-fw pi-bars",
                label: "List",
              },
            ],
          },
        ],
      },
      {
        label: "Events",
        icon: "pi pi-fw pi-calendar",
        items: [
          {
            label: "Edit",
            icon: "pi pi-fw pi-pencil",
            items: [
              {
                label: "Save",
                icon: "pi pi-fw pi-calendar-plus",
              },
              {
                label: "Delete",
                icon: "pi pi-fw pi-calendar-minus",
              },
            ],
          },
          {
            label: "Archieve",
            icon: "pi pi-fw pi-calendar-times",
            items: [
              {
                label: "Remove",
                icon: "pi pi-fw pi-calendar-minus",
              },
            ],
          },
        ],
      },
      {
        label: "Quit",
        icon: "pi pi-fw pi-power-off",
        command: (e) => this.reRouteToLogin(),
      },
    ];
  }

  public backToLogin() {
    // this is logout/ clean everything
    this.vanity_name = "";
    this.subscriptionPlan = {};
    this.client = {};
    this.router.navigate(["login"]);
  }

  public reRouteToPricing() {
    if (
      this.userType === Constants.RECRUITER ||
      this.userType === Constants.COMPANY
    ) {
      this.router.navigate(["company-dashboard"], {
        queryParams: { pricing: "base" },
      });
    } else {
      this.router.navigate(["payment"], {
        queryParams: { optionType: "regular" },
      });
    }
  }

  private rerouteTasks(): void {
    // remove from storage.

    this.localStorageService.removeData("appUser");

  }

  public reRouteToLogin() {
    this.rerouteTasks();
    this.localStorageService.removeData("appUser");
    // this.deleteCookie('jwt');
    this.router.navigate(["login"]);
    
  }

  // deleteCookie(name: string) {
  //   document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
  // }
  
  redirectTo(uri: string) {
    this.router.navigateByUrl("/", { skipLocationChange: true }).then(() => {
      this.router.navigate([uri]);
    });
  }

  public reRouteToHome() {
    // console.log('this.vanity_name = ', this.vanity_name);
    // console.log('this.appUser = ', this.appUser);
    // console.log('this.userType = ', this.userType);

    if (this.userType === Constants.CLIENT) {
      // this.router.navigate(['resume-preview'],{ queryParams: {vanity_name: this.appUser.vanity_name}})
    } else if (this.userType === Constants.COMPANY) {
      this.redirectTo("company-dashboard");
    } else {
      this.redirectTo("alignment");
    }
  }

  get TOOLTIP_DEFAULT_POSITION() {
    return Constants.TOOLTIP_DEFAULT_POSITION;
  }

  refreshPage() {
    location.reload();
  }

  public cancelSubscriptionPlan(): void {
    let payload: any = {};
    payload.sub_id = this.subscriptionPlan.sub_id;
    this.subscription = this.userService
      .cancelSubscriptionPlan(payload)
      .subscribe({
        next: (response) => {
          if (response) {
            setTimeout(() => {
              // reload
              this.refreshPage();
            }, 2000);
          }
        },
        error: (error) => {
          XcvUtilsService.handleError(error, this.messageService);
        },
      });
  }

  public getTokenStatusColor() {
    let color = "";
    if (this.client) {
      let tokenLinit = Number(this.client.tokens_limit);
      let tokenConsumed = Number(this.client.tokens_consumed);

      if (tokenConsumed <= tokenLinit) {
        color = "status_green";
      } else {
        color = "status_red";
      }
    }
    return color;
  }

  public showPricing(): boolean {
    return true;
  }

  public isClientValid(): boolean {
    if (this.client) {
      let tokenLinit = Number(this.client.tokens_limit);
      let tokenConsumed = Number(this.client.tokens_consumed);
      if (tokenLinit > 0) {
        return true;
      } else {
        return false;
      }
    }
    return false;
  }

  public clientLogin(): void {
    this.rerouteTasks();
    this.router.navigate(["login"]);
  }

  ngOnDestroy(): void {
    if (this.subscription) {
      this.subscription.unsubscribe;
    }
  }

  toggleNavbar() {
    this.isNavbarExpanded = !this.isNavbarExpanded;
  }

  onDocumentClick(event: MouseEvent) {
    if (
      this.isNavbarExpanded &&
      !(event.target as HTMLElement).closest(".navbar-collapse")
    ) {
      this.isNavbarExpanded = false;
    }
  }
}
