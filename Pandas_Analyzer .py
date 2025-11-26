#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Visualizer:

    # Proper constructor
    def __init__(self):
        self.data = None

    # ---------------- LOAD DATA ---------------- #
    def load_Data(self):
        path = input("Enter your file path (CSV File): ")

        try:
            if path.endswith(".csv"):
                self.data = pd.read_csv(path)
            else:
                print("Unsupported file format. Please use .csv")
                return

            print("Data loaded successfully!\n")
            print(self.data)

        except Exception as e:
            print(f"Failed to load dataset: {e}")

    # ---------------- EXPLORE DATA ---------------- #
    def explore_data(self):
        print("=" * 10, "Explore Data", "=" * 10)
        print("1. display first 5 rows")
        print("2. display last 5 rows")
        print("3. display column names")
        print("4. display data types")
        print("5. display basic info\n")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print(self.data.head())
            elif choice == 2:
                print(self.data.tail())
            elif choice == 3:
                print(self.data.columns)
            elif choice == 4:
                print(self.data.dtypes)
            elif choice == 5:
                print(self.data.info())
            else:
                print("Invalid choice. Please enter between 1 to 5.")

        except Exception as e:
            print(f"Failed to explore dataset: {e}")

    # ---------------- DATAFRAME OPERATION ---------------- #
    def df_operation(self):
        print("\n========== Perform DataFrame Operation ===========")
        print("1. Filter integer data")
        print("2. Filter float data")
        print("3. Groupby")
        print("4. Minimum Value")
        print("5. Maximum Value")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                column = input("Enter your integer column name to filter: ")
                value = int(input("Enter value to filter: "))
                print(self.data[self.data[column] > value])

            elif choice == 2:
                column = input("Enter your float column name to filter: ")
                value = float(input("Enter value to filter: "))
                print(self.data[self.data[column] > value])

            elif choice == 3:
                column = input("Enter column name to group by: ")
                if column in self.data.columns:
                    print(self.data.groupby(column).size())
                else:
                    print("Column not found!")

            elif choice == 4:
                print("Minimum values:\n", self.data.min(numeric_only=True))

            elif choice == 5:
                print("Maximum values:\n", self.data.max(numeric_only=True))

            else:
                print("Invalid choice. Enter 1 to 5.")

        except Exception as e:
            print(f"Error: {e}")

  
    def missing_data(self):
        print("===== Handle Missing Data =====")
        print("1. display missing values count")
        print("2. fill missing values with mean")
        print("3. drop rows with missing values")
        print("4. replace missing values with specific value\n")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print(self.data.isnull().sum())

            elif choice == 2:
                print("It only fills numerical columns!")
                label = input("Enter column name: ")
                self.data[label].fillna(self.data[label].mean(), inplace=True)
                print(self.data[label])

            elif choice == 3:
                label = input("Enter column name to drop null rows: ")
                self.data = self.data[self.data[label].notna()]
                print("Null values removed!")

            elif choice == 4:
                value = input("Enter value to replace missing entries with: ")
                self.data.fillna(value, inplace=True)
                print(self.data)

            else:
                print("Invalid choice. Enter 1 to 4.")

        except Exception as e:
            print(f"Failed to handle missing data: {e}")

    
    def generate(self):
        print(self.data.describe())

   
    def data_visualization(self):

        print("\n========== Data Visualization ==========")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                A = input("Enter x-axis column: ")
                B = input("Enter y-axis column: ")
                F = input("Enter title: ")
                G = input("Enter legend name: ")
                sns.barplot(data=self.data, x=A, y=B, label=G)
                plt.title(F)
                plt.legend()
                plt.show()

            elif choice == 2:
                A = input("Enter x-axis column: ")
                B = input("Enter y-axis column: ")
                F = input("Enter title: ")
                G = input("Enter legend name: ")
                plt.plot(self.data[A], self.data[B], linestyle="--", marker="o")
                plt.title(F)
                plt.legend([G])
                plt.show()

            elif choice == 3:
                A = input("Enter x-axis column: ")
                B = input("Enter y-axis column: ")
                D = input("Enter hue column: ")
                sns.scatterplot(data=self.data, x=A, y=B, hue=D)
                plt.show()

            elif choice == 4:
                A = input("Enter column name: ")
                plt.pie(self.data[A], autopct="%1.1f%%")
                plt.show()

            elif choice == 5:
                A = input("Enter column name: ")
                sns.histplot(self.data[A])
                plt.show()

            elif choice == 6:
                A = input("Enter x-axis column: ")
                B = input("Enter y-axis column: ")
                plt.stackplot(self.data[A], self.data[B])
                plt.show()

            else:
                print("Invalid choice. Enter 1 to 6.")

        except Exception as e:
            print(f"Failed to visualize data: {e}")

    
    def save_visualization(self):
        A = input("Enter x-axis column: ")
        B = input("Enter y-axis column: ")
        C = input("Enter title: ")
        filename = input("Enter filename (e.g., plot.png): ")

        plt.plot(self.data[A], self.data[B])
        plt.title(C)
        plt.savefig(filename, dpi=4000, bbox_inches='tight')
        print(f"Plot saved as {filename}")



X = Visualizer()

while True:
    print("=" * 10, "Data Analysis & Visualization Program", "=" * 10)
    print("1. Load dataset")
    print("2. Explore data")
    print("3. DataFrame operations")
    print("4. Handle missing data")
    print("5. Generate descriptive statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")

    try:
        press = int(input("Choose option: "))

        if press == 1:
            X.load_Data()
        elif press == 2:
            X.explore_data()
        elif press == 3:
            X.df_operation()
        elif press == 4:
            X.missing_data()
        elif press == 5:
            X.generate()
        elif press == 6:
            X.data_visualization()
        elif press == 7:
            X.save_visualization()
        elif press == 8:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Enter 1 to 8.")

    except Exception as e:
        print(f"Error: {e}")


# In[ ]:


C:\Users\Mohit\Downloads\tips.csv
    


# In[11]:





# In[12]:





# In[ ]:





# In[ ]:




