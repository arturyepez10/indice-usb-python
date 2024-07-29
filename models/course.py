
class Course:

  def __init__(self, code: str, name: str, credits: int, grade: int, removed: bool = False, has_effect: bool = True):
    self.code = code
    self.name = name
    self.credits = credits
    self.grade = grade

    self.has_effect = has_effect
    self.removed = removed


  def __str__(self):
    return f"{self.code} - {self.name} - {self.credits} | removed: {self.removed} | has_effect: {self.has_effect}"