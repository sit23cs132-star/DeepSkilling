# Week 4 – Frontend Frameworks

This directory contains starter projects demonstrating components, state management, and props across React, Angular, and Vue for Week 4 of the FSE Deep Skilling program.

## Directory Contents

### 1. React Application (`React_App/`)
A modular React application using functional components, hooks (`useState`), and custom props.
- `src/App.js` → Main component hosting State.
- `src/CourseList.js` → Sub-component receiving and rendering data via Props.
- `package.json` → App dependencies and start scripts.

### 2. Angular Application (`Angular_App/`)
A structured Angular application showcasing modules, components, and data binding directives.
- `src/app/app.module.ts` → Root Angular Module.
- `src/app/app.component.ts` → Root template shell.
- `src/app/course-list.component.ts` → Child Component containing custom event handling (`click`) and directive (`*ngFor`).

### 3. Vue Application (`Vue_App/`)
A Vue 3 application built with Single File Components (SFCs), templates, and custom properties.
- `src/App.vue` → Parent component containing state methods.
- `src/CourseList.vue` → Child component displaying courses using `v-for`.

---

## How to Run

### React App
```bash
cd React_App
npm install
npm start
```

### Angular App
```bash
cd Angular_App
npm install
npm run start
```

### Vue App
```bash
cd Vue_App
npm install
npm run serve
```
