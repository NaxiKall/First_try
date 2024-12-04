description = 'Woman , 51 years old , born on August 12 , 1971'
description_split = description.split(" , ")
gender = description_split[0].lower().strip()
age = description_split[1].split()
year_of_birth = description_split[3]
print(gender, age[0], year_of_birth)