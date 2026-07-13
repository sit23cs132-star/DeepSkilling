from fastapi import FastAPI
from schemas import CourseCreate, CourseResponse

app = FastAPI(title="Course Management API")

courses = []

@app.get("/api/courses/", response_model=list[CourseResponse])
async def get_courses():
    return courses

@app.post("/api/courses/", response_model=CourseResponse)
async def create_course(course: CourseCreate):
    courses.append(course.dict())
    return course
