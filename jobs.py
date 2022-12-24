from schedule import every, repeat
import schedule
import time

@repeat(every(1).seconds, msg = "Hey Nandy")
def job1(msg):
    print("My Job ran success", msg)

# Schedule job

# job_instance = schedule.every(1).seconds.do(job1)

c = 0
while True:
    schedule.run_pending()
    time.sleep(1)
    c+=1
    # if(c==10):
    #     schedule.cancel_job(job_instance)
