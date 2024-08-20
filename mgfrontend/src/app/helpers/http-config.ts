import { HttpHeaders, HttpParams } from '@angular/common/http';
import { XcvUtils } from './xcv-utils';

const hubUtils = new XcvUtils();

const headerJson = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-user-time-zone': hubUtils.defineTimezoneName()
  };

  const headerFormData = {
};

export const contentHeaders = new HttpHeaders(headerJson);

export const contentHeadersFormData = new HttpHeaders(headerFormData);

export class AytHttpParams {
    params: HttpParams;
  
    constructor() {
      this.params = new HttpParams();
    }
  
    public set(param: string, value: string) {
      this.params = this.params.set(param, value);
    }
  
    public getParams(): HttpParams {
      return this.params;
    }
  
    /**
     * This wil hide the spinner from the ui for an API call
     * usage
     *    const params = new AytHttpParams();
     *    params.disableSpinner();
     *    and pass the params into API service method
     * */
    public disableSpinner() {
      this.params = this.params.set('spinner', 'false');
    }
  }