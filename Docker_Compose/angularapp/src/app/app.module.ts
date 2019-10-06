import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { UserComponent } from './user/user.component';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './home/home.component';
import { AdminComponent } from './admin/admin.component';
import { PmComponent } from './pm/pm.component';
import { RouterModule } from '@angular/router';

import { httpInterceptorProviders } from './auth/auth-interceptor';
import { AppheaderComponent } from './appheader/appheader.component';
import { AppmenuComponent } from './appmenu/appmenu.component';
import { AppsettingComponent } from './appsetting/appsetting.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { AppfooterComponent } from './appfooter/appfooter.component';
import { ApploginComponent } from './applogin/applogin.component';
import { AppregisterComponent } from './appregister/appregister.component';

import { TwitterDataService } from './services/twitterData.service';

import * as $ from 'jquery';

@NgModule({
  exports: [AppfooterComponent],
  declarations: [
    AppComponent,
    LoginComponent,
    UserComponent,
    RegisterComponent,
    HomeComponent,
    AdminComponent,
    PmComponent,
    AppheaderComponent,
    AppmenuComponent,
    AppsettingComponent,
    DashboardComponent,
    AppfooterComponent,
    ApploginComponent,
    AppregisterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    RouterModule
  ],
  providers: [httpInterceptorProviders, TwitterDataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
