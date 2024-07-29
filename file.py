from os.path import isfile

from models import AcademicSummary, AcademicPeriod, Course

class DataReader:

  def __init__(self):
    self.summary = AcademicSummary()
    self.file_path = None

  def _read_line(self, line: str):
    line = line.split(",")
    if not line:
      return []
    
    # We type the elements of the line to correspond to the expected types
    grade = int(line[4]) if line[4] != "R" else None
    return [int(line[0]), line[1], line[2], int(line[3]), grade, line[5]]
  
  def _save_Line(self, line: list):
    if len(self.summary.academic_periods) == line[0] - 1:
      self.summary.add_academic_period(AcademicPeriod())

    period : AcademicPeriod = self.summary.academic_periods[line[0] - 1]

    period.add_course(
      Course(
        code=line[1],
        name=line[2],
        credits=line[3],
        grade=line[4],
        removed=True if line[5].strip() == "Retirada" else False,
        has_effect=False if line[5].strip() == "Sin Efecto" else True
      )
    )

  def load_file(self, file_path: str):
    """ Load a file into the class.

    It verifies if the file exists and sets the file_path variable.
    """
    if isfile(file_path):
      self.file_path = file_path
      return True
    return False
  
  def read_file(self):
    if not self.file_path:
      raise ValueError("File path not set. Please load a file first.")

    with open(self.file_path, 'r') as file:
      for index, line in enumerate(file):
        if index == 0:
          continue
        else:
          elements = self._read_line(line)
          self._save_Line(elements)