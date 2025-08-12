import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

# Generate synthetic warehouse usage data
def generate_synthetic_data(minutes=1440):
    timestamps = [datetime.now() - timedelta(minutes=i) for i in range(minutes)][::-1]
    cpu_usage = np.random.normal(loc=50, scale=20, size=minutes).clip(0, 100)
    memory_usage = np.random.normal(loc=60, scale=25, size=minutes).clip(0, 100)
    auto_scaling_events = [random.choice([0, 1]) if random.random() < 0.01 else 0 for _ in range(minutes)]
    data = pd.DataFrame({
        'Timestamp': timestamps,
        'CPU_Usage': cpu_usage,
        'Memory_Usage': memory_usage,
        'AutoScalingEvent': auto_scaling_events
    })
    return data

# Analyze warehouse efficiency
def analyze_efficiency(data):
    idle_time = data[data['CPU_Usage'] < 10].shape[0]
    over_provisioned_time = data[data['Memory_Usage'] < 30].shape[0]
    auto_scaling_events = data['AutoScalingEvent'].sum()
    recommendations = []
    if idle_time > 60:
        recommendations.append("Consider reducing active hours or consolidating workloads to minimize idle time.")
    if over_provisioned_time > 60:
        recommendations.append("Review memory allocation and consider right-sizing resources.")
    if auto_scaling_events > 20:
        recommendations.append("Optimize auto-scaling policies to reduce unnecessary scaling events.")
    summary = {
        'Idle Time (minutes)': idle_time,
        'Over-Provisioned Time (minutes)': over_provisioned_time,
        'Auto-Scaling Events': auto_scaling_events,
        'Recommendations': recommendations
    }
    return summary

# Visualize usage metrics
def visualize_metrics(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Timestamp'], data['CPU_Usage'], label='CPU Usage (%)')
    plt.plot(data['Timestamp'], data['Memory_Usage'], label='Memory Usage (%)')
    plt.xlabel('Time')
    plt.ylabel('Usage (%)')
    plt.title('Warehouse CPU and Memory Usage Over Time')
    plt.legend()
    plt.tight_layout()
    plt.savefig("warehouse_usage_plot.png")
    plt.close()

# Main execution
data = generate_synthetic_data()
summary = analyze_efficiency(data)
visualize_metrics(data)

# Print summary
print("Warehouse Efficiency Analysis Summary:")
for key, value in summary.items():
    if isinstance(value, list):
        for rec in value:
            print(f"- {rec}")
    else:
        print(f"{key}: {value}")
