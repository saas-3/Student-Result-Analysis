 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("education_impact_on_students.csv")
print(df.head())

df.describe
df.info

df.isnull().sum()

df=df.drop("Unnamed: 0", axis=1)
print(df.head())

df["WklyStudyHours"]=df["WklyStudyHours"].str.replace("05-Oct","5-10")
df.head()

plt.figure(figsize=(4,3))
sns.countplot(data=df,x="Gender")
plt.title("Gender Distribution")

plt.show()

gb=df.groupby("ParentEduc").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
sns.heatmap(gb)
plt.title("Parents education relation with student Scores")
sns.heatmap(gb , annot=True)
plt.show()


gb1=df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
sns.heatmap(gb1)
plt.title("Parents Marital Status relation with student Scores")
sns.heatmap(gb , annot=True)
plt.show()


sns.boxplot(data=df ,x="MathScore")
plt.show()

sns.boxplot(data=df ,x="ReadingScore")
plt.show()

sns.boxplot(data=df ,x="WritingScore")
plt.show()

print(df["EthnicGroup"].unique())
groupA=df.loc[(df['EthnicGroup'] == "group A")].count()

groupB=df.loc[(df['EthnicGroup'] == "group B")].count()

groupC= df.loc[(df['EthnicGroup'] == "group C")].count()

groupD=df.loc[(df['EthnicGroup'] == "group D" )].count()

groupE=df.loc[(df['EthnicGroup'] == "group E")].count()


# Count each ethnic group
counts = df["EthnicGroup"].value_counts()

# Print counts (optional)
print(counts)

# Plot pie chart
plt.pie(counts, labels=counts.index, autopct="%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()