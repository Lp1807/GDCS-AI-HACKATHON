import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AppComponent} from "./app.component";
import { HomeComponent } from './home/home.component'; // Import the HomeComponent


export const routes: Routes = [
  { path: '', component: AppComponent },
  { path: 'home', component: HomeComponent } // Define a route for the "home" page

  // other routes...
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }


