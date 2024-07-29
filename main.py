from models import Course, AcademicPeriod, AcademicSummary
from file import DataReader

first_period = (
  "Abril-Julio", 2016,
  [
    Course("MA1111", "Matematicas I", 4, 3),
    Course("CSA211", "Sociales I", 3, 5),
    Course("LLA111", "Lenguaje I", 3, 3),
    Course("ID1111", "Ingles I", 3, 5),
    Course("MA1511", "Curso de Geometria", 2, 1)
  ]
)

second_period = (
  "Septiembre-Diciembre", 2016,
  [
    Course("MA1112", "Matematicas II", 4, 2),
    Course("FS1111", "Fisica I", 3, 1),
    Course("CSA212", "Sociales II", 3, 3),
    Course("LLA112", "Lenguaje II", 3, 4),
    Course("ID1112", "Ingles II", 3, 5),
  ]
)

def main():
  reader = DataReader()
  reader.load_file("expediente.csv")
  reader.read_file()

  summary = reader.summary

  for index, period in enumerate(summary.academic_periods):
    print(f"Period {index + 1}")
    print(f"\tTotal credits: {period.total_credits}")
    print(f"\tPeriod grade: {period.period_grade}")
    print()

  print("total credits:", summary.total_credits)
  print("total grade:", summary.summary_grade())

if __name__ == "__main__":
  main()