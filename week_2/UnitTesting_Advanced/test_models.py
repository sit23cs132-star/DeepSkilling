import pytest
from courses.models import Course

@pytest.mark.django_db
def test_course_model_str():
    course = Course.objects.create(name="Algorithms", code="CS101", credits=4)
    assert str(course) == "Algorithms"
