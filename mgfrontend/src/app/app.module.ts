import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';
import {DatePipe} from '@angular/common';
import {CurrencyPipe} from '@angular/common';
import { ButtonModule } from 'primeng/button';
import { ConfirmDialogModule } from 'primeng/confirmdialog';
import { DialogModule } from 'primeng/dialog';
import { ToastModule } from 'primeng/toast';
import { DropdownModule } from 'primeng/dropdown';
import { AvatarModule } from 'primeng/avatar';
import { AvatarGroupModule } from 'primeng/avatargroup';
import { CardModule } from 'primeng/card';
import { CalendarModule } from 'primeng/calendar';
import { CheckboxModule } from 'primeng/checkbox';
import { TooltipModule } from 'primeng/tooltip';
import { EditorModule } from 'primeng/editor';
import { ListboxModule } from 'primeng/listbox';
import { TableModule } from 'primeng/table';
import { TabViewModule } from 'primeng/tabview';
import { PasswordModule } from 'primeng/password';
import { MenubarModule } from 'primeng/menubar';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { CarouselModule } from 'primeng/carousel';
import { InputSwitchModule } from 'primeng/inputswitch';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ListDrivesComponent } from './list-drives/list-drives.component';
import { ConfirmationService } from 'primeng/api';
import { RecruiterLoginComponent } from './recruiter-login/recruiter-login.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { CompanyRegisterComponent } from './company-register/company-register.component';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { MultiSelectModule } from 'primeng/multiselect';
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    ListDrivesComponent,
    RecruiterLoginComponent,
    ResetPasswordComponent,
    NotFoundComponent,
    CompanyRegisterComponent,
  ],
  imports: [
    InputSwitchModule,
    CarouselModule,
    NgxChartsModule,
    MenubarModule,
    PasswordModule,
    TabViewModule,
    TableModule,
    ListboxModule,
    EditorModule,
    TooltipModule,
    CheckboxModule,
    CalendarModule,
    CardModule,
    AvatarModule,
    AvatarGroupModule,
    DropdownModule,
    ToastModule,
    BrowserAnimationsModule,
    ButtonModule,
    DialogModule,
    ConfirmDialogModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    NgbModule,
    MultiSelectModule
  ],
  providers: [ConfirmationService, DatePipe, CurrencyPipe,
    { provide: 'apiKey', useValue: 'YOUR_API_KEY' },
    { provide: 'authorize', useValue: 'true' }, 
    { provide: 'isServer', useValue: 'true' }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
