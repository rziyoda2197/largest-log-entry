def top_log_entry(log):
    return max(log, key=lambda x: len(x))

# Misol:
log = [
    "2022-01-01 12:00:00 INFO: Server started",
    "2022-01-01 12:01:00 WARNING: User logged in",
    "2022-01-01 12:02:00 ERROR: Database connection failed",
    "2022-01-01 12:03:00 INFO: User logged out"
]

print(top_log_entry(log))
```

```python
def top_log_entry(log):
    return max(log, key=len)

# Misol:
log = [
    "2022-01-01 12:00:00 INFO: Server started",
    "2022-01-01 12:01:00 WARNING: User logged in",
    "2022-01-01 12:02:00 ERROR: Database connection failed",
    "2022-01-01 12:03:00 INFO: User logged out"
]

print(top_log_entry(log))
