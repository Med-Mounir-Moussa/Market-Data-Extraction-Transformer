import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';

import {API_URL} from '../env';
import { Website } from '../website';
import { Observable } from '../../../node_modules/rxjs/internal/Observable';

@Injectable({
  providedIn: 'root'
})
export class WebsiteFormService {

  constructor(private http: HttpClient) { }

  getDataBase(): Observable<Object> {
    return this.http
      .get('/api/G');
  }

  putInDataBase(url, XPATH1, XPATH2: String){
   return this.http.post('/api/P',["url","XPATH1","XPATH2"]);

  }
}

