def howMany(aDict):
  length = 0
  for e in aDict:
    length += len(aDict[e])
  return length

def biggest(aDict):
  big = aDict.keys()[0]
  for e in aDict:
    if len(aDict[e]) > len(aDict[big]):
      big = e
  return big
