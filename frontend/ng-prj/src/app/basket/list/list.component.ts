

import { Component, OnInit } from '@angular/core';

import { ApiService } from './../../api.service';
import { BasketService } from './../../basket.service';
import { LoginService } from '../../login.service';

import { AuthService } from "angularx-social-login";
import { GoogleLoginProvider } from "angularx-social-login";


@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {

  basket = [];
  isAuth = false;

  constructor(
    private apiService: ApiService,
    private basketService: BasketService,
    private loginService: LoginService,
    private authService: AuthService
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
      products: []
    };
    for(let p of this.basket) {
      req_data.products.push({product: p.id, ammount: 1});
    }
    this.apiService.submitBasket(req_data).subscribe((data: any) => {
      this.basket = [];
      alert('Ваш заказ отправлен, ждите когда с вами свяжется продавец.');
    });
  }

}
