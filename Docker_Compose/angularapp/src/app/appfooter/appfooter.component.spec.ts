import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AppfooterComponent } from './appfooter.component';


import { RouterTestingModule } from '@angular/router/testing';

describe('AppfooterComponent', () => {
  let component: AppfooterComponent;
  let fixture: ComponentFixture<AppfooterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AppfooterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {

    TestBed.configureTestingModule({
    declarations: [
      AppfooterComponent
    ],
    imports: [
      RouterTestingModule
    ]})
    fixture = TestBed.createComponent(AppfooterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
