from datetime import datetime
def timer(start_time):
    return (start_time-datetime.now()).total_seconds()

