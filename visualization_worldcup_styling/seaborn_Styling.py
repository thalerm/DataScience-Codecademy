from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv("WorldCupMatches.csv")
df_goals=pd.read_csv('goals.csv')

#print(df.head())
print(df_goals.head())

df['Total Goals']=df['Home Team Goals'] + df['Away Team Goals']

#print(df.head())
sns.set_style("whitegrid")
sns.set_context('poster', font_scale=0.4)
sns.barplot(data=df, x='Year', y='Total Goals')
#plt.show()
plt.close()

sns.set_context('poster', font_scale=0.7)
f, ax=plt.subplots(figsize=(12, 7))
sns.barplot(data=df, x='Year', y='Total Goals')
ax.set_title('Total Worldcup Goals each Year')
#plt.show()
plt.close()

sns.set_context('notebook', font_scale=1.25)
f, ax2 = plt.subplots(figsize=(12,7))
sns.boxplot(data=df_goals, x='year', y='goals')
ax2.set_title('Total Worldcup Goals each Year')
plt.show()