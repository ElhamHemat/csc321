# Set this variable to 1 for debugging purposes
debug = 0

# This is needed to process command line arguments

import sys            

# The following imports are needed for the same reasons as in gs.py

import copy
import numpy as np
import time

# Check if the command is in the expected format. Exit otherwise.

if(len(sys.argv)!=2):
  print("Invalid syntax. Expected format : \"python gs1.py n\" or \"python gs1.py 25\"")
  sys.exit()

# n = Number of suitors.

n = int(sys.argv[1])

if(n<=0):
  print("Number of suitors must be positive. Please try again.")
  sys.exit()

# The command from the terminal is fine. Do the rest.

def dprint(str):
  if(debug==1):
    print(str)


# Participants - The Professor has asked us to use integers. So,
# the participants will be 1,2,3,....,n

men = []*n 
women = []*n

for i in range(n):
  men.append(i+1)
  women.append(i+1)

# No need to print the participants because they are integers.

men_pref ={}
women_pref ={}

# GS ALgorithm

def GSAlgo(guys, gals):

  dprint("\n\nIntermediate steps : Proposals and dumps :- \n-------------------------------------------------\n")

  # All guys are free
  guysfree = guys[:] 

  # Since all guys are free, the engaged dictionary is empty.     
  engaged  = {}
  men_pref2 = copy.deepcopy(men_pref)
  women_pref2 = copy.deepcopy(women_pref)

  # While there is a free guy, keep doing :

  while guysfree:
    # Consider the first guy who is not yet engaged. This guy is 'guy'
    guy = guysfree.pop(0)

    # Take his preference list of women
    guyslist = men_pref2[guy]

    # Look at which girl he likes the most
    gal = guyslist.pop(0)
    fiance = engaged.get(gal)

    # If that girl is not engaged to any man yet, make the engagement.
    if not fiance:
      engaged[gal] = guy
      if(debug==1):
        print("%s proposes to %s. They are engaged." % (guy, gal))
    else:

      # She is engaged to someone. Take her preference list
      galslist = women_pref2[gal]

      # If she likes 'guy' more than the man she is engaged to right now, she can dump him
      if galslist.index(fiance) > galslist.index(guy):
        engaged[gal] = guy
        if(debug==1):
          print("%s dumped %s for %s" % (gal, fiance, guy))

        # The dumped guy is free now
        if men_pref2[fiance]:
          guysfree.append(fiance)
      else:
        if guyslist:
          guysfree.append(guy)
  return engaged

# Start the timer
start_time = time.time()

# For each run, generate a new preference list for men and women
# Simultaneously, display the preference lists for this iteration

# (i) Generate preferences for men

if(debug==1):
  print("Mens' preference lists : \n-----------------------------------\n")
men_pref = {}
for i in range(0,n):
    rp = np.random.permutation(n)
    temp =  []
    for j in range(0,n):
      temp.append(women[rp[j]])
    men_pref[men[i]] = temp
    if(debug==1):
      print(men[i]," : ",men_pref[men[i]]) 

# (ii) Generate preferences for women

if(debug==1):
  print("\n\nWomens' preference lists : \n-----------------------------------\n")
women_pref = {}
for i in range(0,n):
    rp = np.random.permutation(n)
    temp =  []
    for j in range(0,n):
      temp.append(men[rp[j]])
    women_pref[women[i]] = temp 
    if(debug==1):
      print(women[i]," : ",women_pref[women[i]])

# Now, run the GS algorithm, and print the marriages.
guys = sorted(men_pref.keys())
gals = sorted(women_pref.keys())

engaged = GSAlgo(guys, gals)
dprint('\nFinal result of the GS algorithm:\n---------------------------------------\n')
if(debug==1):
  print(engaged)


# Print the time taken for this iteration
print("%s %s" % (n, time.time() - start_time))
