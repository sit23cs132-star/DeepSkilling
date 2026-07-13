from django.test import TestCase
from .models import Course, Department

class CourseTestCase(TestCase):
    def setUp(self):
        dept = Department.objects.create(name="CS", head_of_dept="Dr. Rao", budget=500000)
        Course.objects.create(name="DSA", code="CS201", credits=4, department=dept)

    def test_course_creation(self):
        course = Course.objects.get(code="CS201")
        self.assertEqual(course.name, "DSA")
