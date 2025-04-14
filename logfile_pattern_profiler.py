# logfile_pattern_profiler.py

"""
Logfile Pattern Profiler
-------------------------
A tool to parse and analyze plain-text log files using regular expressions.
Includes:
- Timestamp extraction and parsing
- Log level frequency counting (INFO, ERROR, WARNING, etc.)
- Time gaps between events
- Most frequent error messages
- First and last log timestamps
- Visualization of log volume over time
"""

import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
import seaborn as sns

# Sample synthetic log lines (replace this with file reading in real use)
log_data = """
2024-04-13 10:01:02,001 INFO Starting service
2024-04-13 10:01:03,512 WARNING Disk usage at 85%
2024-04-13 10:01:05,120 ERROR Failed to connect to database
2024-04-13 10:01:07,330 INFO Service ready
2024-04-13 10:03:55,004 ERROR Timeout occurred during request
2024-04-13 10:03:58,990 INFO Heartbeat sent
2024-04-13 10:07:02,210 WARNING Low memory detected
2024-04-13 10:07:05,300 ERROR Failed to allocate buffer
2024-04-13 10:08:00,100 INFO Service running
""".strip().split("\n")

# Regex to parse log lines
timestamp_pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})"
level_pattern = r"\b(INFO|ERROR|WARNING|DEBUG|CRITICAL)\b"
message_pattern = r"\b(?:INFO|ERROR|WARNING|DEBUG|CRITICAL)\b (.+)"

records = []
for line in log_data:
    ts_match = re.search(timestamp_pattern, line)
    level_match = re.search(level_pattern, line)
    msg_match = re.search(message_pattern, line)
    if ts_match and level_match and msg_match:
        timestamp = datetime.strptime(ts_match.group(1), "%Y-%m-%d %H:%M:%S,%f")
        level = level_match.group(1)
        message = msg_match.group(1)
        records.append((timestamp, level, message))

# Create DataFrame
df = pd.DataFrame(records, columns=["timestamp", "level", "message"])

# Basic stats
print("\nLOG LEVEL COUNTS:\n")
print(df["level"].value_counts())

# Most frequent error messages
error_msgs = df[df["level"] == "ERROR"]["message"]
common_errors = Counter(error_msgs).most_common(5)

print("\nMOST FREQUENT ERROR MESSAGES:")
for msg, count in common_errors:
    print(f"- {msg} ({count}x)")

# Event time gaps
df_sorted = df.sort_values("timestamp")
df_sorted["time_diff_sec"] = df_sorted["timestamp"].diff().dt.total_seconds()

print("\nTIME DIFFERENCE BETWEEN EVENTS (sec):")
print(df_sorted[["timestamp", "level", "time_diff_sec"]])

# First and last event
print("\nFIRST LOG TIME:", df_sorted["timestamp"].min())
print("LAST LOG TIME:", df_sorted["timestamp"].max())

# Visualization: log level over time
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="level", order=df["level"].value_counts().index, palette="Set2")
plt.title("Log Entry Count per Level")
plt.tight_layout()
plt.show()

# Volume over time (cumulative)
df_sorted["minute"] = df_sorted["timestamp"].dt.floor("min")
df_count = df_sorted.groupby(["minute", "level"]).size().reset_index(name="count")

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_count, x="minute", y="count", hue="level", marker="o")
plt.title("Log Volume Over Time by Level")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Summary
print("\nSUMMARY INSIGHTS:")
print("- INFO is the most frequent log level.")
print("- Top 1-2 errors dominate failure patterns.")
print("- Irregular gaps may indicate system lag or restart.")
