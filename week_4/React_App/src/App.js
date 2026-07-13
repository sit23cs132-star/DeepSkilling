import React, { useState } from "react";
import CourseList from "./CourseList";

function App() {
  const [courses, setCourses] = useState([]);

  const addCourse = () => {
    setCourses([...courses, { name: "React Basics", code: "RE101" }]);
  };

  return (
    <div>
      <h1>React Course Manager</h1>
      <button onClick={addCourse}>Add Course</button>
      <CourseList courses={courses} />
    </div>
  );
}

export default App;
