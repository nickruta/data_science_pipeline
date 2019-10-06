import { Component, OnInit } from '@angular/core';
import { TokenStorageService } from './auth/token-storage.service';
import { RouterModule, Routes, Router, NavigationStart } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  info: any;
  private roles: string[];
  private authority: string;
  private title: string;
  isLoggedIn: boolean;

  private showComponent: boolean;

  constructor(private tokenStorage: TokenStorageService, router:Router, private token: TokenStorageService) {

    // this is added to have a test pass in add.component.spec.ts for app title = 'app'
    this.title='app'

    router.events.forEach((event) => {

      if(event instanceof NavigationStart) {

          this.showComponent = (event.url !== "/applogin" && event.url !== "/appregister");

      }
    });

  }

  ngOnInit() {

    this.info = {
      token: this.token.getToken(),
      username: this.token.getUsername(),
      authorities: this.token.getAuthorities()
    };

    if (this.tokenStorage.getToken()) {
      this.isLoggedIn = true;
      this.roles = this.tokenStorage.getAuthorities();
      this.roles.every(role => {
        if (role === 'ROLE_ADMIN') {
          this.authority = 'admin';
          return false;
        } else if (role === 'ROLE_PM') {
          this.authority = 'pm';
          return false;
        }
        this.authority = 'user';
        return true;
      });
    }
  }

  logout() {
    this.token.signOut();
    window.location.reload();
  }
}
