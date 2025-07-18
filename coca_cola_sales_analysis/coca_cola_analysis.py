import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# === Create output folder ===
if not os.path.exists("output"):
    os.makedirs("output")

# === Coca-Cola Sales Data ===
data = {
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Sales_Revenue_Billion_USD": [31.9, 37.3, 33.0, 38.7, 43.0],
    "Volume_Sold_Billion_Liters": [29.2, 30.5, 28.1, 31.4, 33.0],
    "Avg_Bottle_Price_USD": [1.2, 1.25, 1.3, 1.35, 1.4]
}

df = pd.DataFrame(data)

print("🥤 Coca-Cola Global Sales Data:\n")
print(df)

total_revenue = df["Sales_Revenue_Billion_USD"].sum()
avg_volume = np.mean(df["Volume_Sold_Billion_Liters"])
growth_rate = ((df["Sales_Revenue_Billion_USD"].iloc[-1] - df["Sales_Revenue_Billion_USD"].iloc[0]) / df["Sales_Revenue_Billion_USD"].iloc[0]) * 100

print("\n📈 Basic Analysis:")
print(f"➡ Total Revenue (2018-2022): ${total_revenue:.2f} Billion")
print(f"➡ Average Volume Sold: {avg_volume:.2f} Billion Liters")
print(f"➡ Growth Rate from 2018 to 2022: {growth_rate:.2f}%")

plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["Sales_Revenue_Billion_USD"], marker='o', color='red', label="Revenue (Billion USD)")
plt.title("Coca-Cola Global Revenue Trend")
plt.xlabel("Year")
plt.ylabel("Revenue (Billion USD)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("output/revenue_trend.png")
plt.show()

plt.figure(figsize=(8,5))
plt.bar(df["Year"], df["Volume_Sold_Billion_Liters"], color='green')
plt.title("Coca-Cola Volume Sold (Billion Liters)")
plt.xlabel("Year")
plt.ylabel("Volume Sold (Billion Liters)")
plt.tight_layout()
plt.savefig("output/volume_sold.png")
plt.show()
