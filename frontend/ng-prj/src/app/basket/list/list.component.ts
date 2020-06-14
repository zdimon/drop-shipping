

import { Component, OnInit } from '@angular/core';

import { ApiService } from './../../api.service';
import { BasketService } from './../../basket.service';
import { LoginService } from '../../login.service';

import { AuthService } from "angularx-social-login";
import { GoogleLoginProvider } from "angularx-social-login";
import { Router } from '@angular/router';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {

  basket = [];
  isAuth = false;
  phone = '';

  constructor(
    private apiService: ApiService,
    private basketService: BasketService,
    private loginService: LoginService,
    private authService: AuthService,
    private router: Router
    ) {

    this.apiService.getBasketInfo(this.basketService.getBasket()).subscribe((rez: any) => {
      this.basket = rez;
    });

    this.loginService.isAuth$.subscribe(data => {
      this.isAuth = data;
   });


   }

  ngOnInit() {
  }


  signInWithGoogle(): void {
    this.authService.signIn(GoogleLoginProvider.PROVIDER_ID).then(res => {
       this.authService.authState.subscribe(user => {
          this.apiService.loginByGoogle(user).subscribe((rez) => {
            this.loginService.login(rez);
          })
       })
    });
  }

  submitBasket() {
    let req_data = {
      products: [],
      phone: this.phone
    }; 
    for(let p of this.basket) {
      req_data.products.push({product: p.id, ammount: p.ammount});
    }
    this.apiService.submitBasket(req_data).subscribe((data: any) => {
      this.basket = [];
      this.basketService.submitBasket();
      alert('Ваш заказ отправлен, ждите когда с вами свяжется продавец.');
      this.router.navigate(['/']);
    });
  }

  ammountUp(id: number){
    for(let i of this.basket) {
      if(i.id === id) {
        i.ammount += 1;
      }
      console.log(i);
    }
  }

  ammountDown(id: number){
    for(let i of this.basket) {
      if(i.id === id) {
        i.ammount -= 1;
      }
      console.log(i);
    }
  }

  delete(id: number){
    for(let i of this.basket) {
      if(i.id === id) {
        this.basket.splice( this.basket.indexOf(i),1);
      }
      console.log(i);
    }
  }

}
