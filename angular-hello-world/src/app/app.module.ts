import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HelloWorldComponent } from './hello-world/hello-world.component';
import { HelloComponent } from './hello/hello.component';
import { NewComponent } from './new/new.component';

@NgModule({
  declarations: [
    AppComponent,
    HelloWorldComponent,
    HelloComponent,
    NewComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
