import { Component } from '@angular/core';

@Component({
  selector: 'app-course-list',
  template: `
    <ul>
      <li *ngFor="let course of courses">{{ course.name }} ({{ course.code }})</li>
    </ul>
    <button (click)="addCourse()">Add Course</button>
  `
})
export class CourseListComponent {
  courses = [{ name: "Angular Basics", code: "AN101" }];

  addCourse() {
    this.courses.push({ name: "New Course", code: "AN102" });
  }
}
