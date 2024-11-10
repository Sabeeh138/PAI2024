import matplotlib.pyplot as plt

# Sample data: ice cream flavors and the number of scoops sold
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough']
scoops_sold = [500, 300, 150, 100, 200]
plt.pie(scoops_sold, labels=flavors, autopct='%1.1f%%', startangle=140, colors=['#ffcc99', '#ff9966', '#ff6666', '#99cc99', '#66b3ff'])
plt.title('Distribution of Ice Cream Sales')
plt.show()
