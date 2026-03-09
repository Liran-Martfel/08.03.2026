#create a tuple with 3 of your favorite movies
movies:tuple = 'endgame','the pursuit after happiness','man in black'
print(movies)

# 2 create tuple with all countries in Europe (ask ChatGPT)
countries = ["Albania", "Andorra", "Austria", "Belarus", "Belgium",
    "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czechia", "Denmark",
    "Estonia", "Finland", "France", "Germany", "Greece",
    "Hungary", "Iceland", "Ireland", "Italy", "Latvia",
    "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova",
    "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway",
    "Poland", "Portugal", "Romania", "Russia", "San Marino",
    "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden",
    "Switzerland", "Ukraine", "United Kingdom", "Vatican City"]
countries = tuple(countries)
print(countries)

# 3 create tuple with all the days of feb (1, 2 ... 28)
days_in_feb = []
for days in range(1,29):
    days_in_feb.append(days)
days_in_feb = tuple(days_in_feb)
print(days_in_feb)

# 4 create tuple with all the days of dec (1, 2 ... 31)
days_in_dec = []
for days in range(1,32):
    days_in_dec.append(days)
days_in_feb = tuple(days_in_dec)
print(days_in_dec)

# 5 create tuple of all the month in the year
month_in_year = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
month_in_year = tuple(month_in_year)
print(month_in_year)

# 6 create tuple of all USA presidents till today (ask ChatGPT), use len to find out how many are they

us_presidents = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison",
    "James Monroe", "John Quincy Adams", "Andrew Jackson", "Martin Van Buren",
    "William Henry Harrison", "John Tyler", "James K. Polk", "Zachary Taylor",
    "Millard Fillmore", "Franklin Pierce", "James Buchanan", "Abraham Lincoln",
    "Andrew Johnson", "Ulysses S. Grant", "Rutherford B. Hayes", "James A. Garfield",
    "Chester A. Arthur", "Grover Cleveland", "Benjamin Harrison", "Grover Cleveland",
    "William McKinley", "Theodore Roosevelt", "William Howard Taft", "Woodrow Wilson",
    "Warren G. Harding", "Calvin Coolidge", "Herbert Hoover", "Franklin D. Roosevelt",
    "Harry S. Truman", "Dwight D. Eisenhower", "John F. Kennedy", "Lyndon B. Johnson",
    "Richard Nixon", "Gerald Ford", "Jimmy Carter", "Ronald Reagan",
    "George H.W. Bush", "Bill Clinton", "George W. Bush", "Barack Obama",
    "Donald Trump", "Joe Biden", "Donald Trump"]

president = len(us_presidents)
us_presidents = tuple(us_presidents)
print(president)


# 7 use mean to find the avg of this tuple = (8, 11, -3, 12)
numbers = (8,11,-3,12)
avg = (sum(numbers)/len(numbers))
avg = int(avg)
print(avg)
