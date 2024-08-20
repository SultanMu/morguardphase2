import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListDrivesComponent } from './list-drives.component';

describe('ListDrivesComponent', () => {
  let component: ListDrivesComponent;
  let fixture: ComponentFixture<ListDrivesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ListDrivesComponent]
    });
    fixture = TestBed.createComponent(ListDrivesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
