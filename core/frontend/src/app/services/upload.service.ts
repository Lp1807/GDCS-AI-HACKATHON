import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UploadService {
  url = 'http://127.0.0.1:8080/';

  constructor(private http: HttpClient) { }


  uploadFile(data: { [key: string]: any }): Observable<any> {
    console.log(data)
    return this.http.post(this.url, data);
  }
 }
