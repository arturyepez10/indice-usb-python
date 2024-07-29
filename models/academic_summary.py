from .academic_period import AcademicPeriod

class AcademicSummary:

  def __init__(self):
    self.academic_periods: list[AcademicPeriod] = []

  def add_academic_period(self, academic_period: AcademicPeriod):
    self.academic_periods.append(academic_period)

  @property
  def total_credits(self):
    return sum([academic_period.total_credits for academic_period in self.academic_periods])
  
  @property
  def total_credits_passed(self):
    return sum([academic_period.total_credits_passed for academic_period in self.academic_periods])
  
  def summary_grade(self):
    valid_courses = [period.get_valid_courses() for period in self.academic_periods]

    credits_enrolled = 0
    notes_factor = 0.0

    for period in valid_courses:
      for course in period:
        credits_enrolled += course.credits
        notes_factor += course.grade * course.credits

    return notes_factor / credits_enrolled if credits_enrolled > 0 else 0.0
