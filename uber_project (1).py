#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv(r"C:\Users\rohit\OneDrive\Desktop\uber-raw-data-aug14.csv")

df.head()


# In[ ]:





# #### Q1. On what date did we see the most number of Uber pickups?
# 
# **Skill Test:** Grouping & Counting

# In[ ]:


# Convert the 'Date/Time' column to datetime format
df["Date/Time"]=pd.to_datetime(df["Date/Time"])

# Group by date and count the number of pickups
pickup=df.groupby(df['Date/Time'].dt.date).count()
pickup.head(1)

# Find the date with the highest number of pickups
highest=pickup.sort_values(by='Lat',ascending=False)
highest.index[0]
print("highest pickup happend on",highest.index[0])





# In[3]:


df.dtypes


# #### Q.2 How many Uber pickups were made on the date with the highest number of pickups?
# 
# **Skill Test:** Indexing and filtering

# In[5]:


# Filter the DataFrame to include only the rows for the date with the highest number of pickups

df[df['Date/Time'].dt.date==highest.index[0]]



# Get the count of pickups on the highest date
df['Date'] = df['Date/Time'].dt.date

# Group by the Date column and count the number of pickups
pickup_counts = df.groupby('Date').size()

# Find the maximum value
max_pickup_count = pickup_counts.max()

print(f"The highest number of pickups on a single date is {max_pickup_count}.")


# #### Q.3 How many unique TLC base companies are affiliated with the Uber pickups in the dataset?
# 
# **Skill Test:** Counting unique values

# In[6]:


# Count the number of unique TLC base companies
unique_company=df['Base'].nunique()
print("No of companies affiliates with Uber-",unique_company)


# #### Q.4 Which TLC base company had the highest number of pickups?
# 
# **Skill Test:** Grouping, counting, and finding the maximum

# In[11]:


# Group by TLC base company and count the number of pickups
df.groupby(df['Date/Time'].dt.date)['Base'].count()
# Find the TLC base company with the highest number of pickups

base_pickups = df.groupby('Base').size()
base_pickups


# #### Q.5 How many Uber pickups were made at each unique TLC base company?
# 
# **Skill Test:** Grouping and counting

# In[8]:


# Group by TLC base company and count the number of pickups

result = df.groupby('Base').size().reset_index(name='Pickup Count')

print(result)



# #### Q.6 Can you determine the busiest time of day for Uber pickups based on the date/time column?
# 
# **Skill Test:** Extracting time components, grouping, counting, and finding the maximum

# In[22]:


# Extract the hour from the 'Date/Time' column

df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['Hour'] = df['Date/Time'].dt.hour

print(df)
# Group by hour and count the number of pickups
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['Hour'] = df['Date/Time'].dt.hour
print(df['Hour'].value_counts())
print(df.groupby('Hour').size())


# Find the hour with the highest number of pickups

# Convert the Date/Time column to a datetime object
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Extract the hour from the Date/Time column
df['Hour'] = df['Date/Time'].dt.hour

# Group by the Hour column and count the number of pickups
pickup_counts = df.groupby('Hour').size()

# Find the index of the maximum value
max_pickup_hour = pickup_counts.idxmax()

print(f"The hour with the highest number of pickups is {max_pickup_hour}.")


# #### Q.7 Can you create a visualization (e.g., a bar chart or line plot) to represent the number of Uber pickups over time?
# 
# **Skill Test:** Data Visualization using Plotting function

# In[23]:


import matplotlib.pyplot as plt

# Group by date and count the number of pickups

x=df['Date/Time'].dt.date.value_counts()
x
# Create a line plot to visualize the number of pickups over time
x=df['Date/Time'].dt.date.value_counts()
x


# #### Q8. Can you create a scatter plot to visualize the distribution of Uber pickups based on latitude and longitude?
# 
# **Skill Test:** Scatter Plot

# In[24]:


# Create a scatter plot to visualize the distribution of Uber pickups based on latitude and longitude
plt.scatter(df['Lat'],df["Lon"])


# #### Q9. Can you create a bar chart to compare the number of Uber pickups for each TLC base company?
# 
# **Skill Test:** Bar Chart

# In[25]:


# Create a bar chart to compare the number of Uber pickups for each TLC base company
x=df['Base'].value_counts()
x.plot(kind='bar')


# #### Q10. Can you create a pie chart to display the percentage distribution of Uber pickups for each day of the week?
# 
# **Skill Test:** Pie Chart

# In[26]:


# Group by day of the week and count the number of pickups
x=df['Date/Time'].dt.day_name().value_counts()
x

# Create a pie chart to display the percentage distribution of Uber pickups for each day of the week
plt.figure(figsize=(10,7))
plt.pie(x.values, labels = x.index,autopct= '%f')
plt.show()


# In[ ]:




