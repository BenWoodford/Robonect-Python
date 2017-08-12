from robonect.robonect_client import robonect_client

client = robonect_client("10.0.3.11", "root", "homekit123")

status = client.getStatus()
print("Got Status for %s, battery is at %s%%" % (status["name"], status["status"]["battery"]))

#print("Starting Job...")
#client.startJob("00:00", 5)
#print("Job Started")

#print("Ending Day...")
#client.endDay()
#print("Day Ended.")
