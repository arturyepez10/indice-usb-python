import argparse

from models import Course
from file import DataReader

def main(parser: argparse.ArgumentParser):

  parameters = parser.parse_args()

  file_name = parameters.n

  if not parameters.n:
    print("[WARNING] custom name not found for the project")
    file_name = "expediente.csv"

  reader = DataReader()
  reader.load_file(file_name)
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
  parse = argparse.ArgumentParser("Indice Academico | USB")

  parse.add_argument(
    "-name",
    "--n",
    metavar="N",
    help="Nombre del archivo de hoja de cálculo con el expediente",
    required=False
  )

  main(parse)