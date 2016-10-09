from fractions import Fraction

JITEuropeFive = [1/1., 16/15., 9/8., 6/5., 5/4., 4/3., 45/32., 3/2., 8/5., 5/3., 16/9., 15/8.]

JITEuropeSeven = [1/1., 28/27., 9/8., 7/6., 9/7., 4/3., 112/81., 3/2., 14/9., 12/7., 7/4., 16/9. ]

major = [0,2,4,5,7,9,11]

majorSeven = [0,1,3,5,7,8,10]

everyToneAsTonic = []
#everyToneAsTonic+=JITEuropeFive

for tone in range(len(JITEuropeFive)):
  everyToneAsTonic+=[[]]
  for interval in major:
    everyToneAsTonic[len(everyToneAsTonic)-1] += [Fraction(JITEuropeFive[(tone+interval)%len(JITEuropeFive)]/JITEuropeFive[tone]).limit_denominator(1000)]

inverseOfEveryToneAsTonic = []
for scale in range(len(everyToneAsTonic)):
  inverseOfEveryToneAsTonic.append([1])
  for toneInScale in range(1,len(everyToneAsTonic[scale])):
    inverseOfEveryToneAsTonic[len(inverseOfEveryToneAsTonic)-1].append((1/everyToneAsTonic[scale][len(everyToneAsTonic[scale])-1-toneInScale])*2)


for scale in range(len(everyToneAsTonic)):
  for toneInScale in range(len(everyToneAsTonic[scale])):
    if everyToneAsTonic[scale][toneInScale] < 1:
      everyToneAsTonic[scale][toneInScale]*=2
    everyToneAsTonic[scale][toneInScale]=str(everyToneAsTonic[scale][toneInScale])


for scale in range(len(inverseOfEveryToneAsTonic)):
  for toneInScale in range(len(inverseOfEveryToneAsTonic[scale])):
    if inverseOfEveryToneAsTonic[scale][toneInScale] < 1:
      inverseOfEveryToneAsTonic[scale][toneInScale]*=2
    inverseOfEveryToneAsTonic[scale][toneInScale]=str(inverseOfEveryToneAsTonic[scale][toneInScale])


#print 'EVERY JITEuropeFive'
#for scale in range(len(everyToneAsTonic)):
#  print str(everyToneAsTonic[scale])

#print 'EVERY JITEuropeFive Inverse'
#for scale in range(len(inverseOfEveryToneAsTonic)):
#  print str(inverseOfEveryToneAsTonic[scale])

everyToneAsTonic = []
#everyToneAsTonic+=JITEuropeFive

for tone in range(len(JITEuropeSeven)):
  everyToneAsTonic+=[[]]
  for interval in majorSeven:
    everyToneAsTonic[len(everyToneAsTonic)-1] += [Fraction(JITEuropeSeven[(tone+interval)%len(JITEuropeSeven)]/JITEuropeSeven[tone]).limit_denominator(1000)]

inverseOfEveryToneAsTonic = []
for scale in range(len(everyToneAsTonic)):
  inverseOfEveryToneAsTonic.append([1])
  for toneInScale in range(0,len(everyToneAsTonic[scale])-1):
    inverseOfEveryToneAsTonic[len(inverseOfEveryToneAsTonic)-1].append((1/everyToneAsTonic[scale][len(everyToneAsTonic[scale])-1-toneInScale])*2)


for scale in range(len(everyToneAsTonic)):
  for toneInScale in range(len(everyToneAsTonic[scale])):
    if everyToneAsTonic[scale][toneInScale] < 1:
      everyToneAsTonic[scale][toneInScale]*=2
    everyToneAsTonic[scale][toneInScale]=str(everyToneAsTonic[scale][toneInScale])


for scale in range(len(inverseOfEveryToneAsTonic)):
  for toneInScale in range(len(inverseOfEveryToneAsTonic[scale])):
    if inverseOfEveryToneAsTonic[scale][toneInScale] > 2:
      inverseOfEveryToneAsTonic[scale][toneInScale]/=2
    inverseOfEveryToneAsTonic[scale][toneInScale]=str(inverseOfEveryToneAsTonic[scale][toneInScale])

print 'EVERY JITEuropeSeven'
for scale in range(len(everyToneAsTonic)):
  print str(everyToneAsTonic[scale])

print 'EVERY JITEuropeSeven Inverse'
for scale in range(len(inverseOfEveryToneAsTonic)):
  print str(inverseOfEveryToneAsTonic[scale])


#for toneAsTonic in range(len(JITEuropeFive)):
#  everyToneAsTonic.append([])
#  for intInScale in range(len(major)):
#    print toneAsTonic, intInScale
#    everyToneAsTonic[len(everyToneAsTonic)-1].append(factorize(JITEuropeFive[((toneAsTonic+major[intInScale])%len(JITEuropeFive))*(2**((toneAsTonic+intInScale)/len(JITEuropeFive)))]/JITEuropeFive[toneAsTonic]))