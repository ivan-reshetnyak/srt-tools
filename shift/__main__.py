from ..util import console
from ..util import logging
from datetime import datetime, timedelta


logging.start()

print("Parsing command line arguments...")
args = console.parse()
missing = list(console.missing_keys("input", "output", "shift", args=args))
if missing:
    logging.terminate("Missing parameters: %s" % missing, -1)

print("Working...")
delta = timedelta(seconds=int(args["shift"]))
with open(args["input"], encoding="utf8") as fileIn, open(args["output"], "w+", encoding="utf8") as fileOut:
    while fileIn:
        fileOut.write(fileIn.readline())  # Popup number, just copy
        timesStr = fileIn.readline().strip().split(" --> ")  # Line with times, split in beginning/end
        if len(timesStr) < 2:
            # File over
            break
        timesOut = []
        print(timesStr)
        for timeStr in timesStr:
            time = datetime.strptime(timeStr, "%H:%M:%S,%f")
            time += delta
            timesOut.append(time.strftime("%H:%M:%S,%f"))
        fileOut.write(" --> ".join(timesOut) + "\n")

        strIn = fileIn.readline()
        while len(strIn) > 0 and strIn != "\n":
            fileOut.write(strIn)
            strIn = fileIn.readline()
        else:
            fileOut.write(strIn)

logging.finish()
