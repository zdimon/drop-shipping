import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EditComponent } from './edit/edit.component';
import { RouterModule, Routes } from '@angular/router';
import { NotificationComponent } from './notification/notification.component';


import {MatButtonModule} from '@angular/material/button';
import { FlexLayoutModule } from '@angular/flex-layout';


const routes: Routes = [

  { path: '', component: EditComponent},
  { path: 'notify', component: NotificationComponent}

];


@NgModule({
  declarations: [EditComponent, NotificationComponent],
  imports: [
    CommonModule,
    RouterModule.forChild(routes),
    MatButtonModule,
    FlexLayoutModule
  ]
})
export class ProfileModule { }
