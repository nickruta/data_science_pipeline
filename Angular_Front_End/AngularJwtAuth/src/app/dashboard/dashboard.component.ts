import { Component, OnInit } from '@angular/core';

import { TokenStorageService } from '../auth/token-storage.service';
import {ActivatedRoute, Router} from '@angular/router';



@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
})
export class DashboardComponent implements OnInit {

  info: any;

  constructor(private token: TokenStorageService, private route:ActivatedRoute,private router:Router) { }

  ngOnInit() {



    this.info = {
      token: this.token.getToken(),
      username: this.token.getUsername(),
      authorities: this.token.getAuthorities()
    };


   // if (this.token.roles.length < 1) {
  //    this.router.navigate(['applogin']);
   // }

   // console.log(this)

  }

  logout() {
    this.token.signOut();
    this.router.navigate(['/applogin'])
  }

}

