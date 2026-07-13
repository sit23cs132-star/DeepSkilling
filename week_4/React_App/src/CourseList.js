import React from "react";

function CourseList({ courses }) {
  return (
    <ul>
      {courses.map((c, i) => (
        <li key={i}>{c.name} ({c.code})</li>
      ))}
    </ul>
  );
}

export default CourseList;
