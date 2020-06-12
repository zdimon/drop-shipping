
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListComponent } from './list/list.component';

import { RouterModule, Routes } from '@angular/router';

import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import { FlexLayoutModule } from '@angular/flex-layout';

import { ApiService } from './../api.service';
import { AddComponent } from './add/add.component';

import { FormsModule } from '@angular/forms';

import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material';
import {MatSelectModule} from '@angular/material/select';
import { CameraComponent } from './camera/camera.component';
import {MatDialogModule} from '@angular/material/dialog';


const routes: Routes = [

  { path: '', component: ListComponent},
  { path: 'cat/:catId', component: ListComponent},
  { path: 'subcat/:SubCatId', component: ListComponent},
  { path: 'add', component: AddComponent}

];

@NgModule({
  declarations: [ListComponent, AddComponent, CameraComponent],
  imports: [
    CommonModule,
    RouterModule.forChild(routes),
    MatButtonModule,
    MatCardModule,
    FlexLayoutModule,
    FormsModule,

    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatDialogModule
  ],
  providers: [
    ApiService
  ],
  entryComponents: [
    CameraComponent
  ]
})
export class CatalogModule { }
