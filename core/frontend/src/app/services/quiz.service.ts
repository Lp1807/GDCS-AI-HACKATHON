import { Injectable } from '@angular/core';
import { QuizQuestion } from '../models/quiz-question';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class QuizQuestionService {
  url = 'http://127.0.0.1:8080/quiz';

  constructor(private http: HttpClient) { }

getQuizQuestion(id: Number): Observable<any> {
    return this.http.get(this.url + '/' + id);
  }
 }
