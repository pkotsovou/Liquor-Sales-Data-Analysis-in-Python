import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Φόρτωση των δεδομένων (περίοδος 2012-2020)
url = "https://storage.googleapis.com/courses_data/Assignment%20CSV/finance_liquor_sales.csv"
df = pd.read_csv(url)

# Προεπισκόπηση των αρχικών δεδομένων
print("Προεπισκόπηση αρχικών δεδομένων:")
print(df.head())

# Μετατροπή της στήλης 'date' σε τύπο datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Φιλτράρισμα των δεδομένων για την περίοδο 2016-2019
df_filtered = df[(df['date'].dt.year >= 2016) & (df['date'].dt.year <= 2019)]
print("\nΔεδομένα μετά το φιλτράρισμα για τα έτη 2016-2019:")
print(df_filtered.head())

# Έλεγχος για ελλείπουσες τιμές σε όλες τις στήλες
print("\nΈλεγχος για ελλείπουσες τιμές σε όλες τις στήλες:")
print(df_filtered.isnull().sum())

# Αφαίρεση όλων των γραμμών που περιέχουν ελλείπουσες τιμές
df_filtered = df_filtered.dropna()

print("\nΔεδομένα μετά την αφαίρεση γραμμών με ελλείπουσες τιμές:")
print(df_filtered.info())

# Καθαρισμός της στήλης 'zip_code' και μετατροπή της σε ακέραιο αριθμό
df_filtered['zip_code'] = df_filtered['zip_code'].astype(int)

# Μετατροπή αριθμητικών στηλών σε σωστούς τύπους
df_filtered['bottles_sold'] = df_filtered['bottles_sold'].astype(int)
df_filtered['sale_dollars'] = df_filtered['sale_dollars'].astype(float)

# Τελική επισκόπηση των καθαρισμένων δεδομένων
print("\nΠληροφορίες για τα καθαρισμένα δεδομένα:")
print(df_filtered.info())
print("\nΠροεπισκόπηση των καθαρισμένων δεδομένων:")
print(df_filtered.head())

# Task 1: Εύρεση του πιο δημοφιλούς προϊόντος ανά Zip Code

# Ομαδοποίηση κατά zip_code και item_number, υπολογισμός συνολικών πωλήσεων (bottles_sold)
popular_items = df_filtered.groupby(['zip_code', 'item_number'])['bottles_sold'].sum().reset_index()

# Εύρεση για κάθε zip_code του προϊόντος (item_number) με τις περισσότερες πωλήσεις (bottles_sold)
most_popular_per_zip = popular_items.loc[popular_items.groupby('zip_code')['bottles_sold'].idxmax()]

print("\nΠιο δημοφιλές προϊόν (με βάση το item_number) ανά Zip Code:")
print(most_popular_per_zip)

# Visualization for Task 1

# Seaborn Scatter Plot - Bottles Sold Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(x=most_popular_per_zip.index,  # Άξονας Χ το index
                y=most_popular_per_zip['bottles_sold'],
                alpha=0.7, legend=None)

# Προσθήκη ετικετών για τις κουκίδες που έχουν bottles_sold > 200
for i in range(len(most_popular_per_zip)):
    if most_popular_per_zip['bottles_sold'].iloc[i] > 200:
        plt.annotate(most_popular_per_zip['item_number'].iloc[i],
                     (most_popular_per_zip.index[i], most_popular_per_zip['bottles_sold'].iloc[i]),
                     textcoords="offset points", xytext=(0, 10), ha='center')

plt.title('Bottles Sold', fontsize=16)
plt.xlabel('Index', fontsize=14)
plt.ylabel('Bottles Sold', fontsize=14)
plt.tight_layout()
plt.show()

# Task 2: Υπολογισμός ποσοστού συνολικών πωλήσεων ανά κατάστημα

# Υπολογισμός του συνολικού ποσού πωλήσεων για κάθε κατάστημα
sales_per_store = df_filtered.groupby(['store_number', 'store_name'])['sale_dollars'].sum().reset_index()

# Υπολογισμός του συνολικού ποσού πωλήσεων για όλα τα καταστήματα
total_sales = sales_per_store['sale_dollars'].sum()

# Υπολογισμός του ποσοστού πωλήσεων ανά κατάστημα
sales_per_store['sales_percentage'] = (sales_per_store['sale_dollars'] / total_sales) * 100

# Προεπισκόπηση των αποτελεσμάτων
print("\nΠοσοστά πωλήσεων ανά κατάστημα:")
print(sales_per_store)

# Visualization for Task 2

# Plotly Bar Chart - Sales Percentage Visualization
fig = px.bar(sales_per_store,
             x='sales_percentage',
             y='store_name',
             orientation='h',
             title='%Sales by Store',
             labels={'sales_percentage': 'Sales(%)', 'store_name': 'Store Name'},
             color='sales_percentage',  # Χρώμα ανάλογα με το sales_percentage
             color_continuous_scale='Viridis',  # Παλέτα χρωμάτων
             text='sales_percentage')  # Εμφάνιση ποσοστού στις μπάρες

fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(title_x=0.5)
fig.show()