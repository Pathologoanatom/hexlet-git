def capitalize (name):
  No_space_name = name.strip()
  return f"{No_space_name[0].upper()}{No_space_name[1:]}"




def capitalize(str=" Непустая строка"):
  str = str.strip().capitalize()
  return str
