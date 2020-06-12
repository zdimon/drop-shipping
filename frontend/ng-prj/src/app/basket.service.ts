import { Injectable } from '@angular/core';

import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BasketService {

  private _basket = [];

  basket$ = new BehaviorSubject([]);


  constructor() { }

  addToBasket(id: number) {
    if(!this.isInBasket(id)) {
      this._basket.push(id);
    }
    this.basket$.next(this._basket);
  }

  getBasket(){
    return this._basket;
  }

  isInBasket(value) {
    return this._basket.indexOf(value) > -1;
  }

  delFromBasket() {
    this.basket$.next(this._basket);
  }

  submitBasket() {

  }

}
