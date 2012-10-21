def oddTuples(aTup):
  oddT= ()
  for i in range(len(aTup)):
    if (i % 2 == 0):
      oddT += (aTup[i],)
  return oddT
