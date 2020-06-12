
import { Injectable } from '@angular/core';
import { environment } from './../environments/environment';

import { ReplaySubject } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SocketService {

  private socket: any;

  public updater$ = new ReplaySubject();


  constructor() {

    this.socket = new WebSocket(`${environment.socketUrl}/market`);
    this.dispatcher();
   }


   dispatcher(): void {
     this.socket.onmessage = (event) => {
       const message = JSON.parse(event.data);

      if(message.action === 'update_notify') {
        this.updater$.next(message);
      }

     }
   }
}
