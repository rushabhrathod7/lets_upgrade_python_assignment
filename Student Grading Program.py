def calculate_grade(marks):
  """Calculates and returns the grade for a given set of marks."""

  if marks >= 90:
    grade = "A+"
  elif marks >= 80:
    grade = "A"
  elif marks >= 70:
    grade = "B"
  elif marks >= 60:
    grade = "C"
  elif marks >= 50:
    grade = "D"
  else:
    grade = "Fail"

  return grade


def main():
  """The main function of the program."""

  while True:
    # Get the marks from the user.
    marks = int(input("Enter the marks: "))

    # Check if the marks are valid.
    if marks < 0 or marks > 100:
      print("Invalid marks. Please enter marks between 0 and 100.")
      continue

    # Calculate and display the grade.
    grade = calculate_grade(marks)
    print("The grade for {} marks is {}".format(marks, grade))

    # Check if the user wants to exit.
    prompt = "Do you want to calculate the grade for another student? (y/n): "
    answer = input(prompt).lower()
    if answer != "y":
      break


if __name__ == "__main__":
  main()
