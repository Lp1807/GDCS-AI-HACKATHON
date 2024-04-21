import { Component } from '@angular/core';
import {RouterOutlet} from "@angular/router";
import {HttpClient} from "@angular/common/http";
import {QuizQuestion} from "../models/quiz-question";
import * as http from "http";
import {QuizQuestionService} from "../services/quiz.service";

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

  constructor(private http: HttpClient, private quizQuestionService: QuizQuestionService,
) {}
  question = "ciaone"
  currentQuestionID = 0
  currentQuestion = ""
  optionA = ""
  optionB = ""
  optionC = ""
  optionD = ""

  onNgInit(){
    this.getQuestionData()
  }

  getQuestionData(){
    this.quizQuestionService.getQuizQuestion(this.currentQuestionID).subscribe({
      next: (response) => {
        console.info('Question retrieved', response);
        this.currentQuestion = response["question"]
        this.optionA = response["options"]["A"]
        this.optionB = response["options"]["B"]
        this.optionC = response["options"]["C"]
        this.optionD = response["options"]["D"]
      },
      error: (error) => {
        console.error('Error getting question:', error);
      }
    });
  }


  onOptionAClicked(){
    console.log("A clicked")
    this.http.get('http://127.0.0.1:8080/correct/A')
      .subscribe(
        (response) => {
          console.info('Answer correctly retrieved', response);
        },
        (error) => {
          console.error('Error getting result:', error);
        }
      );
  }

  onOptionBClicked(){
  console.log("B clicked")
  this.http.get('http://127.0.0.1:8080/correct/B')
    .subscribe(
      (response) => {
        console.info('Answer correctly retrieved', response);
      },
      (error) => {
        console.error('Error getting result:', error);
      }
    );
  }


  /**
  onOptionCClicked(event: any){
    this.updateAnswer("C");
  }

  onOptionDClicked(event: any){
    this.updateAnswer("D");
  }

  updateAnswer(givenAnswer){
    this.givenAnswer = givenAnswer;
  }
  **/
}
