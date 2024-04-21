import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AppComponent} from "./app.component";
import {ChooseTopicComponent} from "./choose-topic/choose-topic.component";
import {QuizComponent} from "./quiz/quiz.component"; // Import the HomeComponent


export const routes: Routes = [
  { path: '', component: AppComponent },
  { path: 'choose_topic', component: ChooseTopicComponent},
  { path: 'quiz', component: QuizComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }


