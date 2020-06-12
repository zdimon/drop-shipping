

import { Component, OnInit } from '@angular/core';

import { ApiService } from './../../api.service';

import { Router } from '@angular/router';

import { MatDialog } from '@angular/material/dialog';
import { CameraComponent } from './../camera/camera.component';

@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.scss']
})
export class AddComponent implements OnInit {

  cats: any;
  subcats = [];
  name = '';
  price: string;
  image: any;
  image_base64: any;

  constructor(
    private apiService: ApiService,
    private router: Router,
    public dialog: MatDialog
  ) {
      this.apiService.getCategoryList().subscribe((data: any) => {
        this.cats = data;
      })
   }

   addImgFromCam() {
    const dialogRef = this.dialog.open(CameraComponent, {
        width: '450px'
      });
      const sub = dialogRef.componentInstance.onPic.subscribe((data: any) => {
        this.image_base64 = data.imgBase64;
      });

      this.dialog.afterAllClosed.subscribe(
        () => {
          sub.unsubscribe();
        }
      );
  }

  ngOnInit() {
  }

  doCatChange(evt: any) {
    for(let it of this.cats) {
      if(it.id === evt.value) {
        this.subcats = it.subcategory;
      }
    }
  }

  onImageChanged(event: any) {
    this.image = event.target.files[0];
  }

  submitForm() {
    const formData = new FormData();
    formData.append('name', this.name);
    formData.append('price', this.price);
  
    if(this.image) formData.append('image', this.image);
    formData.append('image_base64', this.image_base64);
    this.apiService.addProduct(formData).subscribe((data: any) => {
      console.log(data);
      this.router.navigate(['catalog']);
    })
  }


}
