import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AppComponent} from "./app.component";
import { HomeComponent } from './home/home.component';
import {ChooseTopicComponent} from "./choose-topic/choose-topic.component"; // Import the HomeComponent


export const routes: Routes = [
  { path: '', component: AppComponent },
  { path: 'home', component: HomeComponent },
  { path: 'choose_topic', component: ChooseTopicComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }


