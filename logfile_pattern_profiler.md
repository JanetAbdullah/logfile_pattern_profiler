
# Logfile Pattern Profiler

This Python script parses and analyzes system log files using regular expressions. It is designed to extract key metadata such as timestamps, log levels, and messages, then summarize and visualize patterns in log activity.

## Project Objectives
- Parse timestamps, log levels, and messages from structured logs
- Count frequency of each log level (INFO, ERROR, WARNING, etc.)
- Identify and rank most common error messages
- Calculate time intervals between events
- Visualize log frequency and level distribution over time

## Features
- Supports timestamps in format: `YYYY-MM-DD HH:MM:SS,mmm`
- Parses logs with multiple levels and formats using regex
- Detects irregular time gaps between log entries
- Summarizes first and last recorded events
- Outputs most frequent error messages
- Displays bar and line charts to visualize trends

## Technologies Used
- Python 3.x
- pandas
- matplotlib
- seaborn
- re (Regular Expressions)

## How to Run
1. Install dependencies:
```bash
pip install pandas matplotlib seaborn
```
2. Run the script:
```bash
python logfile_pattern_profiler.py
```

> Note: Replace the synthetic `log_data` list with actual log file lines using file I/O if needed.

## File Structure
```
logfile_pattern_profiler/
├── logfile_pattern_profiler.py   # Main analysis script
├── README.md                     # Documentation and usage
```

## Visual Outputs
- Bar chart: Number of log entries per log level
- Line chart: Volume of log entries over time by level

## Key Insights
- Detects burst errors or irregular activity via timestamps
- Highlights dominant log levels and failure causes
- Offers immediate feedback on log data health and density

## Author
Janet Abdullah  
GitHub: [https://github.com/JanetAbdullah]  
Feel free to fork and extend this tool for real log analysis pipelines.
