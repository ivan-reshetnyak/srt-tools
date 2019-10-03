from ..util import console
from ..util import logging
from datetime import datetime, timedelta


logging.start()

print("Parsing command line arguments...")
args = console.parse()
missing = list(console.missing_keys("input", "output", "first", "last", args=args))
if missing:
    logging.terminate("Missing parameters: %s" % missing, -1)
args["first"] = int(args["first"])
args["last"] = int(args["last"])

print("Working...")
with open(args["input"], encoding="utf-8-sig") as fileIn, open(args["output"], "w+", encoding="utf8") as fileOut:
    while fileIn:
        entryNum = fileIn.readline()
        if len(entryNum) == 0:
            break
        entryNum = int(entryNum)
        if args["first"] <= entryNum <= args["last"]:
            strIn = fileIn.readline()
            while len(strIn) > 0 and strIn != "\n":
                strIn = fileIn.readline()
            continue
            
        if entryNum > args["last"]:
            entryNum -= args["last"] - args["first"] + 1
        fileOut.write(str(entryNum) + "\n")
        
        strIn = fileIn.readline()
        while len(strIn) > 0 and strIn != "\n":
            fileOut.write(strIn)
            strIn = fileIn.readline()
        else:
            fileOut.write(strIn)

logging.finish()
