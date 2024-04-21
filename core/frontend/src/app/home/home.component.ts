import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

  constructor(private http: HttpClient) {}

  onFileSelected(event: any) {
    const file: File = event.target.files[0];
    this.uploadFile(file);
  }

  uploadFile(file: File) {
    const formData: FormData = new FormData();
    formData.append('file', file, file.name);

    this.http.post('http://127.0.0.1:8080/upload/', formData)
      .subscribe(
        (response) => {
          console.info('File uploaded successfully:', response);
          // Handle successful upload here
        },
        (error) => {
          console.error('Error uploading file:', error);
          // Handle upload error here
        }
      );
  }
}
