name = "Tim Rogers"

address = """WeWork,
38 Chancery Lane,
London,
WC2A 1EN"""

age_in_years = 25
age_in_days = age_in_years * 365
age_in_years_1000_days_ago = (age_in_days - 1000) / 365

print "My name is " \
    + name + " and I am " + str(age_in_years) + " years old (that's " \
    + str(age_in_days) + " days). 1000 days ago, I was " \
    + str(age_in_years_1000_days_ago) + " years old. My address is: " \
    + address
