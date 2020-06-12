import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from './../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  getProduclList(pars) {
    if(pars.hasOwnProperty('cat')){
      return this.http.get(`${environment.backendUrl}v1/market/product_list?category=${pars.cat}`);
    }
    if(pars.hasOwnProperty('subcat')){
      return this.http.get(`${environment.backendUrl}v1/market/product_list?subcategory=${pars.subcat}`);
    }
    return this.http.get(`${environment.backendUrl}v1/market/product_list`);
  }

  getCategoryList() {

    return this.http.get(`${environment.backendUrl}v1/market/category_list`);
  }

  getBasketInfo(pars){
    const data = {ids: pars};
    return this.http.post(`${environment.backendUrl}v1/market/basket_list`,data);
  }

  loginByGoogle(data){
    return this.http.post(`${environment.backendUrl}v1/market/google_auth`,data);
  }

  init() {
    return this.http.get(`${environment.backendUrl}v1/market/init`);
  }

  addProduct(data){
    return this.http.post(`${environment.backendUrl}v1/market/add_product`,data);
  }

  submitBasket(data) {
    return this.http.post(`${environment.backendUrl}v1/market/basket_submit`,data);
  }

  notifyList() {
    return this.http.get(`${environment.backendUrl}v1/market/notification_list`);
  }

}
