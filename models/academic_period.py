
from models.course import Course

class AcademicPeriod:
  
  def __init__(self, name: str = "", year: int = None):
    self.name = name
    self.year = year
    self.courses: list[Course] = []

  def add_course(self, course: Course):
    self.courses.append(course)

  def get_valid_courses(self):
    return [course for course in self.courses if not (course.removed or not course.has_effect)]
  
  def get_period_courses(self):
    return [course for course in self.courses if not course.removed]

  @property
  def total_credits(self):
    courses = self.get_period_courses()

    return sum([course.credits for course in courses])
  
  @property
  def total_credits_passed(self):
    return sum([course.credits for course in self.courses if course.grade >= 3])

  def total_credits_by_grade(self, grade: int):
    return sum([course.credits for course in self.courses if course.grade == grade])

  @property
  def period_grade(self):
    courses = self.get_period_courses()

    taken_courses = sum([course.credits for course in courses])

    notes = sum([course.grade * course.credits for course in courses])

    return notes / taken_courses if taken_courses > 0 else 0.0