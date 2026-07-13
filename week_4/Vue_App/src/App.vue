<template>
  <div>
    <h1>Vue Course Manager</h1>
    <button @click="addCourse">Add Course</button>
    <CourseList :courses="courses" />
  </div>
</template>

<script>
import CourseList from "./CourseList.vue";

export default {
  components: { CourseList },
  data() {
    return {
      courses: []
    };
  },
  methods: {
    addCourse() {
      this.courses.push({ name: "Vue Basics", code: "VU101" });
    }
  }
};
</script>
