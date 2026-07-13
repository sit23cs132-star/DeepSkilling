<template>
  <ul>
    <li v-for="(course, index) in courses" :key="index">
      {{ course.name }} ({{ course.code }})
    </li>
  </ul>
</template>

<script>
export default {
  props: ["courses"]
};
</script>
