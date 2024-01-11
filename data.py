from matplotlib import pyplot as plt

years = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
gdp = [3.4, 1.8, 2.0, 2.1, 2.6, 4.6, 8.6, 5.6, 5.4, 3.4, 6.5, 4.6, 7.3, 2.1, 3.4]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.bar(range(len(gdp)), gdp)

plt.title('Nonimal GPD')
plt.xlabel('years')
plt.ylabel('GPD in Billion $')
plt.xticks(range(len(years)), years)

plt.show()