import { Injectable } from '@angular/core';
import { CanActivateFn } from '@angular/router';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { AuthService } from './auth.service';


@Injectable({
  providedIn: 'root',
})

export class AuthGuard implements CanActivate {
  constructor(private authService: AuthService, private router: Router
    ) {}

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    if (this.authService.isLoggedInUser()) {
      return true;
    } else {
      this.router.navigate(['/login']);
      return false;
    }
  }
}

// export const authGuard: CanActivateFn = (route, state) => {
//   return true;
// };
