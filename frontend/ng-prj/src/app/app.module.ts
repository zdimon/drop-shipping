


import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FlexLayoutModule } from '@angular/flex-layout';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { HttpClientModule } from '@angular/common/http';

import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import {MatMenuModule} from '@angular/material/menu';
import {MatIconModule} from '@angular/material/icon';

import { BasketService } from './basket.service';
import {MatBadgeModule} from '@angular/material/badge';

import { SocialLoginModule, AuthServiceConfig } from "angularx-social-login";
import { GoogleLoginProvider } from "angularx-social-login";
import { AuthService } from "angularx-social-login";

import { LoginService } from './login.service';

import { AuthInterceptorService } from './auth-interceptor.service';
import { HTTP_INTERCEPTORS, HttpClient } from '@angular/common/http';

import { SocketService } from './socket.service';

export const interceptorProviders = [
  { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptorService, multi: true }
];


const config = new AuthServiceConfig([
  {
    id: GoogleLoginProvider.PROVIDER_ID,
    provider: new GoogleLoginProvider("769722970237-8lhn2anpmkjjagu1monnvooetln72i2b.apps.googleusercontent.com")
  }
]);

export function provideConfig() {
  return config;
}

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule.withServerTransition({ appId: 'serverApp' }),
    AppRoutingModule,
    FlexLayoutModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatCardModule,
    HttpClientModule,
    MatMenuModule,
    MatIconModule,
    MatBadgeModule

  ],
  providers: [
    BasketService,
    AuthService,
    LoginService,
    {
      provide: AuthServiceConfig,
      useFactory: provideConfig
    },
    AuthInterceptorService,
    interceptorProviders,
    SocketService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
