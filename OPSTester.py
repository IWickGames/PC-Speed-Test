import time
import sys

monitorMode = str(input("Turn Monitor-Mode(True) on or Bentchmark(False)? "))
if monitorMode != 'True':
  if monitorMode != 'False':
    print("You must enter True or False")
    input('Press any key to exit...')
    sys.exit()
runAmount = 20
averageCounter = 0
runNumber = 0

lastMillis = 0
timeRun = 0
runNumber = 0
if monitorMode == 'False':
  while runNumber != runAmount+1:
    millis = int(round(time.time() * 1))
    if millis != lastMillis:
      lastMillis = millis
      print(str(timeRun) + '/ops ' + str(runNumber) + '  Count: ' + str(averageCounter))
      averageCounter += timeRun
      timeRun = 0
      runNumber += 1
    else:
      timeRun += 1
  average = round(averageCounter/runAmount)
  print("Average OPS: " + str(average) + "  Total Operations Performed: " + str(averageCounter))
  a = input("\n\n\n\nPress any key to exit...")
  sys.exit()

if monitorMode == 'True':
  lastTimeRun = 0
  while True:
    millis = int(round(time.time() * 1))
    if millis != lastMillis:
      if timeRun > lastTimeRun:
        message = str(timeRun) + '/ops ' + str(runNumber) + ' Up: ' + str(timeRun-lastTimeRun)
      else:
        message = str(timeRun) + '/ops ' + str(runNumber) + ' Down: ' + str(timeRun-lastTimeRun)
      lastMillis = millis
      print(message)
      lastTimeRun = timeRun
      timeRun = 0
      runNumber += 1
    else:
      timeRun += 1