import matplotlib.pyplot as plt
import numpy as np

# Sample height data for 20 students
students = [f'Student {i+1}' for i in range(20)]
heights = [150, 155, 160, 165, 170, 172, 158, 164, 169, 171,
           173, 168, 162, 166, 159, 161, 157, 174, 163, 167]

# Generate random colors for each bar
colors = plt.cm.viridis(np.linspace(0, 1, len(students)))

# Bar chart
plt.figure(figsize=(10, 6))
plt.bar(students, heights, color=colors)
plt.xlabel('Students')
plt.ylabel('Height (cm)')
plt.title('Bar Chart of Student Heights')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Pie chart

height_ranges = ['150-155 cm', '156-160 cm', '161-165 cm', '166-170 cm', '171-175 cm']
range_counts = [sum(150 <= h <= 155 for h in heights),
                sum(156 <= h <= 160 for h in heights),
                sum(161 <= h <= 165 for h in heights),
                sum(166 <= h <= 170 for h in heights),
                sum(171 <= h <= 175 for h in heights)]

plt.figure(figsize=(8, 8))
plt.pie(range_counts, labels=height_ranges, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Pie Chart of Student Heights Ranges')
plt.show()
