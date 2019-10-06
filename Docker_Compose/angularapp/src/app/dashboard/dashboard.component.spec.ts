import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardComponent } from './dashboard.component';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { RouterModule } from '@angular/router';



describe('DashboardComponent', () => {
  let component: DashboardComponent;
  let fixture: ComponentFixture<DashboardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DashboardComponent ],
      imports: [
      FormsModule, ReactiveFormsModule, HttpClientTestingModule, RouterModule.forRoot([])
    ]
    })
    .compileComponents();
  }));

  beforeEach(() => {

      TestBed.configureTestingModule({
    declarations: [
    ],
    imports: [
      FormsModule, ReactiveFormsModule, HttpClientTestingModule, RouterModule.forRoot([])
    ]})


    fixture = TestBed.createComponent(DashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});




