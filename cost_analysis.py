from prometheus_client import start_http_server, Gauge
import pandas as pd
import time

cloud_cost = Gauge('cloud_estimated_cost', 'Estimated Cloud Cost')

data = {
    "Service": ["Compute", "Storage", "Networking"],
    "Usage": [120, 500, 80],
    "Cost_per_unit": [0.05, 0.02, 0.01]
}

df = pd.DataFrame(data)
df["Total_Cost"] = df["Usage"] * df["Cost_per_unit"]
total = df["Total_Cost"].sum()

print(df)
print("\nTotal Cloud Cost: $", total)

cloud_cost.set(total)
start_http_server(8001)

print("Serving cost metric on :8001 — press Ctrl+C to stop")
while True:
    time.sleep(5)