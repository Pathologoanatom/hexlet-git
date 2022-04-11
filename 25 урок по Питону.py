from datetime import date

# BEGIN (write your solution here)
def get_current_year():
  current_date = f"{date.today().year}"
  print(current_date[0:4])
  return int(current_date)

  get_current_year()

