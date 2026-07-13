import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { CourseListComponent } from './course-list.component';

@NgModule({
  declarations: [AppComponent, CourseListComponent],
  imports: [BrowserModule],
  bootstrap: [AppComponent]
})
export class AppModule {}
