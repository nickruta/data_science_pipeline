import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { ApploginComponent } from './applogin.component';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { RouterModule } from '@angular/router';

describe('ApploginComponent', () => {
  let component: ApploginComponent;
  let fixture: ComponentFixture<ApploginComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ApploginComponent ],
      imports: [
      FormsModule, ReactiveFormsModule, HttpClientTestingModule,
      RouterModule.forRoot([]),
    ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
        TestBed.configureTestingModule({
    declarations: [
    ],
    imports: [
      FormsModule, ReactiveFormsModule, HttpClientTestingModule
    ]})

    fixture = TestBed.createComponent(ApploginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
