import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { RouterModule } from '@angular/router';

import { PmComponent } from './pm.component';

describe('PmComponent', () => {
  let component: PmComponent;
  let fixture: ComponentFixture<PmComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PmComponent ],
      imports: [
      HttpClientTestingModule, RouterModule.forRoot([])
    ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PmComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
