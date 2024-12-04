experience = "Work experience 202 month"
experience_ladno = experience.split()
experience_years = int(experience_ladno[2]) // 12
experience_month = int(experience_ladno[2]) % 12
print(experience_years, experience_month)