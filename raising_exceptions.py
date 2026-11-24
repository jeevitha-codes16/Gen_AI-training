def check_age(age):
    if age < 0:
      raise ValueError("Age cannot be negative.")
    printf("valid age")

check_age(-5)