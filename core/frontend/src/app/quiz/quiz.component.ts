import { Component } from '@angular/core';
import {RouterOutlet} from "@angular/router";

@Component({
  selector: 'app-quiz',
  standalone: true,
    imports: [
        RouterOutlet
    ],
  templateUrl: './quiz.component.html',
  styleUrl: './quiz.component.css'
})
export class QuizComponent {
  givenAnswer = "";
  
  constructor(private http: HttpClient) {}


  onOptionAClicked(event: any){
    this.updateAnswer("A");
  }

  onOptionBClicked(event: any){
    this.updateAnswer("B");
  }

  onOptionCClicked(event: any){
    this.updateAnswer("C");
  }

  onOptionDClicked(event: any){
    this.updateAnswer("D");
  }

  updateAnswer(givenAnswer: str){
    this.givenAnswer = givenAnswer;
  }
}
