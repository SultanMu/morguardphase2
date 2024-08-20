import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { interval, Observable, of } from 'rxjs';
import { switchMap, takeWhile } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class PollingService {
  constructor(private http: HttpClient) {}

  startPolling(
    conditionFn: (response: any) => boolean,
    apiUrl: string,
    queryParams: any,
    intervalTime: number
  ): Observable<any> {
    return interval(intervalTime).pipe(
      switchMap(() => this.http.get(apiUrl, { params: queryParams })),
      takeWhile(response => !conditionFn(response))
    );
  }
}
