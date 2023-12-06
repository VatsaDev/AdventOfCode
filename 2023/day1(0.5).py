inputS="""
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

numsAll = []
for line in inputS.splitlines():
  numA = []
  for j in range(len(line)):
    if line[j] in "123456789":
      numA.append(line[j])

  if(len(numA)>0):
    numsAll.append(numA[0]+numA[-1])

val = 0
for i in range(len(numsAll)):
  val += int(numsAll[i])

print(val)