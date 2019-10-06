import { TestBed, inject } from '@angular/core/testing';

import { TwitterDataService } from './twitterData.service';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';

describe('TwitterDataService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TwitterDataService],
      imports: [
      FormsModule, ReactiveFormsModule, HttpClientTestingModule,RouterModule.forRoot([])
    ]
    });
  });

  it('should be created', inject([TwitterDataService], (service: TwitterDataService) => {
    expect(service).toBeTruthy();
  }));
});
