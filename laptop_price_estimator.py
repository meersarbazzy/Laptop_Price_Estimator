import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from ydata_profiling import ProfileReport

# Load dataset
dataset_path = r"C:\\Users\\Meer Sarbazzy\\Downloads\\laptop_price.csv"

try:
    df = pd.read_csv(dataset_path, encoding='ISO-8859-1')
    df.columns = df.columns.str.strip()
    df['Company'] = df['Company'].str.lower().str.strip()
    df['Product'] = df['Product'].str.lower().str.strip()
    df['Ram'] = df['Ram'].str.lower().str.strip()
    df['Memory'] = df['Memory'].str.lower().str.strip()
    df['Cpu'] = df['Cpu'].str.lower().str.strip()
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Conversion rate
EURO_TO_PKR = 300  # Example conversion rate

# Preprocess dataset
label_encoders = {}
encoded_df = df.copy()

for col in ['Company', 'Product', 'Ram', 'Memory', 'Cpu']:
    le = LabelEncoder()
    encoded_df[col] = le.fit_transform(encoded_df[col])
    label_encoders[col] = le

X = encoded_df[['Company', 'Product', 'Ram', 'Memory', 'Cpu']]
y = encoded_df['Price_euros']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediction function
def calculate_price(company, product, ram, memory, processor):
    try:
        company_encoded = label_encoders['Company'].transform([company])[0]
        product_encoded = label_encoders['Product'].transform([product])[0]
        ram_encoded = label_encoders['Ram'].transform([ram])[0]
        memory_encoded = label_encoders['Memory'].transform([memory])[0]
        processor_encoded = label_encoders['Cpu'].transform([processor])[0]

        features = [[company_encoded, product_encoded, ram_encoded, memory_encoded, processor_encoded]]
        predicted_price = model.predict(features)[0]
        return round(predicted_price, 2)
    except Exception as e:
        subset_df = df[(df['Company'] == company) & (df['Product'] == product) & (df['Cpu'] == processor)]
        if not subset_df.empty:
            return round(subset_df['Price_euros'].mean(), 2)
        return None

# Update dropdown options
def update_options(event):
    company = combo_company.get().lower().strip()
    filtered_df = df[df['Company'] == company]

    combo_product['values'] = filtered_df['Product'].unique().tolist()
    combo_product.set('')
    combo_ram['values'] = filtered_df['Ram'].unique().tolist()
    combo_ram.set('')
    combo_memory['values'] = filtered_df['Memory'].unique().tolist()
    combo_memory.set('')
    combo_processor['values'] = filtered_df['Cpu'].unique().tolist()
    combo_processor.set('')

# Calculate price
def on_calculate():
    company = combo_company.get().lower().strip()
    product = combo_product.get().lower().strip()
    ram = combo_ram.get().lower().strip()
    memory = combo_memory.get().lower().strip()
    processor = combo_processor.get().lower().strip()

    if not (company and product and ram and memory and processor):
        messagebox.showerror("Error", "Please fill all the fields.")
        return

    price_euros = calculate_price(company, product, ram, memory, processor)
    if price_euros:
        price_pkr = round(price_euros * EURO_TO_PKR, 2)
        result_label.config(
            text=f"Estimated Price: \u20ac{price_euros}\nEquivalent Price: PKR {price_pkr}"
        )
    else:
        messagebox.showerror("Error", "Laptop configuration not found.")

# Generate EDA report
def generate_eda():
    profile = ProfileReport(df, title="Laptop Dataset EDA", explorative=True)
    profile.to_file("eda_report.html")
    eda_label.config(text="EDA report has been saved as eda_report.html")

# Main application
root = tk.Tk()
root.title("Laptop Price Estimator")
root.geometry("900x700")
root.configure(bg="#f3f4f6")

# Header
header = tk.Label(root, text="Laptop Price Estimator", font=("Arial", 18, "bold"), bg="#1e3c72", fg="white", pady=10)
header.pack(fill="x")

# Input Frame
frame = tk.Frame(root, bg="#f3f4f6", pady=20)
frame.pack(pady=10, padx=10, fill="x")

# Input Fields
labels = ["Select Laptop Brand:", "Select Laptop Model:", "Select RAM Size:", "Select Storage Type:", "Select Processor:"]
combos = []

for i, label in enumerate(labels):
    tk.Label(frame, text=label, bg="#f3f4f6", font=("Arial", 12), anchor="w").grid(row=i, column=0, pady=5, sticky="w")
    combo = ttk.Combobox(frame, width=30)
    combo.grid(row=i, column=1, pady=5, padx=10)
    combos.append(combo)

combo_company, combo_product, combo_ram, combo_memory, combo_processor = combos
combo_company['values'] = df['Company'].unique().tolist()
combo_company.bind("<<ComboboxSelected>>", update_options)

# Buttons
button_frame = tk.Frame(root, bg="#f3f4f6")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Calculate Price", command=on_calculate, bg="#1e3c72", fg="white", font=("Arial", 12), width=20).grid(row=0, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Generate EDA Report", command=generate_eda, bg="#1e3c72", fg="white", font=("Arial", 12), width=20).grid(row=0, column=1, padx=10, pady=5)

# Result display
result_label = tk.Label(root, text="Estimated Price: \u20ac\nEquivalent Price: PKR", font=("Arial", 14, "bold"), bg="#f3f4f6", fg="#1e3c72")
result_label.pack(pady=20)

eda_label = tk.Label(root, text="", font=("Arial", 12), bg="#f3f4f6", fg="#1e3c72")
eda_label.pack()

root.mainloop()
