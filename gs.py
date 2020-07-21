import copy
import numpy as np
import time

# Participants - I am using the same names as mentioned by the Prof
# in the assignment description document.

men = ['abe','bob','col','dan','ed','fred','gav','hal','ian','john']
women = ['abi','bea','cath','dee','eve','fay','gay','hope','ivy','jan']

men_pref ={}
women_pref ={}

# GS ALgorithm

def GSAlgo(guys, gals):

  print("\n\nIntermediate steps : Proposals and dumps :- \n-------------------------------------------------\n")

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
      print("%s proposes to %s. They are engaged." % (guy, gal))
    else:

      # She is engaged to someone. Take her preference list
      galslist = women_pref2[gal]

      # If she likes 'guy' more than the man she is engaged to right now, she can dump him
      if galslist.index(fiance) > galslist.index(guy):
        engaged[gal] = guy
        print("%s dumped %s for %s" % (gal, fiance, guy))

        # The dumped guy is free now
        if men_pref2[fiance]:
          guysfree.append(fiance)
      else:
        if guyslist:
          guysfree.append(guy)
  return engaged





# Display the participants

print("Participants\n-------------------------")
print("Men: ",men)
print("Women: ",women)

b = True 
while(b):

  # Start the timer
  start_time = time.time()

  # For each run, generate a new preference list for men and women
  # Simultaneously, display the preference lists for this iteration

  # (i) Generate preferences for men
  print("Mens' preference lists : \n-----------------------------------\n")
  men_pref = {}
  for i in range(0,10):
      rp = np.random.permutation(10)
      temp =  []
      for j in range(0,10):
        temp.append(women[rp[j]])
      men_pref[men[i]] = temp
      print(men[i]," : ",men_pref[men[i]]) 

  # (ii) Generate preferences for women
  print("\n\nWomens' preference lists : \n-----------------------------------\n")
  women_pref = {}
  for i in range(0,10):
      rp = np.random.permutation(10)
      temp =  []
      for j in range(0,10):
        temp.append(men[rp[j]])
      women_pref[women[i]] = temp 
      print(women[i]," : ",women_pref[women[i]])

  # Now, run the GS algorithm, and print the marriages.
  guys = sorted(men_pref.keys())
  gals = sorted(women_pref.keys())

  engaged = GSAlgo(guys, gals)
  print('\nFinal result of the GS algorithm:\n---------------------------------------\n')
  print(engaged)


  # Print the time taken for this iteration
  print("--- %s seconds ---" % (time.time() - start_time))

  ch = input("Do you wish to simulate another round ? Enter 'y' for yes, 'n' for no : ")
  if(ch=='n'):
    b = False 

print("Bye! Thank you!")
