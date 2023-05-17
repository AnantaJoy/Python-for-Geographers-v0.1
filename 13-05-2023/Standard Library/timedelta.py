from datetime import datetime, timedelta

# timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
print(timedelta(days=365, hours=5, minutes=1))

# datetime.now() + timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
print(datetime.now() + timedelta(days=365, hours=5, minutes=1))

# datetime.now() - timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
print(datetime.now() - timedelta(days=365, hours=5, minutes=1))

# datetime.now() - datetime.now()
print(datetime.now() - datetime.now())

# datetime.now() - datetime.now() + timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
print(datetime.now() - datetime.now() + timedelta(days=365, hours=5, minutes=1, weeks=3))