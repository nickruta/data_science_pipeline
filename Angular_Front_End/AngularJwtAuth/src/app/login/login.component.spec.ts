import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginComponent } from './login.component';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';



describe('LoginComponent', () => {
  let component: LoginComponent;
  let fixture: ComponentFixture<LoginComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LoginComponent ],
      imports: [
      FormsModule, ReactiveFormsModule, HttpClientTestingModule,RouterModule.forRoot([])
    ]
    })
    .compileComponents();
  }));

  beforeEach(() => {

        TestBed.configureTestingModule({
    declarations: [
    ],
    imports: [
      FormsModule, ReactiveFormsModule, HttpClientTestingModule,RouterModule.forRoot([])
    ]})


    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
