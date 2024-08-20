import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { ListDrivesComponent } from './list-drives/list-drives.component';
import { RecruiterLoginComponent } from './recruiter-login/recruiter-login.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { CompanyRegisterComponent } from './company-register/company-register.component';
import { AuthGuard } from './helpers/auth.guard';

const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'token-expired', component: LoginComponent },
  { path: 'recruiter-login', component: RecruiterLoginComponent },
  { path: 'reset-password', component: ResetPasswordComponent },
  { path: 'password-reset', component: ResetPasswordComponent },
  { path: 'list-drives', component: ListDrivesComponent, canActivate: [AuthGuard]},
  { path: 'company-register', component: CompanyRegisterComponent },
  { path: 'company-login', component: RecruiterLoginComponent },
  { path: 'companylogin', component: RecruiterLoginComponent },

  // { path: 'vanity-name', component: UserDetailsComponent},
  { path: 'vanity-name', component: LoginComponent},
  //{ path: 'template1', component: Template1Component}
  { path: 'not-found', component: NotFoundComponent },  
  { path: '**', redirectTo: '/not-found' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
