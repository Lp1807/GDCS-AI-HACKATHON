import { Component } from '@angular/core';
import {UploadService} from "../services/upload.service";
import {response} from "express";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

  constructor(
    private uploadFileService: UploadService
  ) {}


  uploadFile(data: { [key: string]: any }){
    this.uploadFileService.uploadFile(data).subscribe({
      next: (response) => {
        console.log("Success:", response)
      },
      error: (error) => {
        console.error("Fail:", error)
      }
    })
  }


}


