import copy
import numpy as np

men = ['abe','bob','col','dan','ed','fred','gav','hal','ian','john']
women = ['abi','bea','cath','dee','eve','fay','gay','hope','ivy','jan']

men_pref ={}
women_pref ={}

#Generate preferences for men
for i in range(0,10):
    rp = np.random.permutation(10)
    temp =  []
    for j in range(0,10):
      temp.append(women[j])
    men_pref[men[i]] = temp 

#Generate preferences for women
for i in range(0,10):
    rp = np.random.permutation(10)
    temp =  []
    for j in range(0,10):
      temp.append(men[j])
    women_pref[women[i]] = temp 


guys = sorted(men_pref.keys())
gals = sorted(women_pref.keys())


def check(engaged):
  rev_eng = dict((v,k) for k,v in engaged.items())
  for she, he in engaged.items():
      shelikes = women_pref[she]
      shelikesbetter = shelikes[:shelikes.index(he)]
      helikes = men_pref[he]
      helikesbetter = helikes[:helikes.index(she)]
      for guy in shelikesbetter:
          guysgirl = rev_eng[guy]
          guylikes = men_pref[guy]
          if guylikes.index(guysgirl) > guylikes.index(she):
              print("%s and %s like each other better than "
                    "their present partners: %s and %s, respectively"
                    % (she, guy, he, guysgirl))
              return False
      for gal in helikesbetter:
          girlsguy = engaged[gal]
          gallikes = women_pref[gal]
          if gallikes.index(girlsguy) > gallikes.index(he):
              print("%s and %s like each other better than "
                    "their present partners: %s and %s, respectively"
                    % (he, gal, she, girlsguy))
              return False
  return True

def GSAlgo():
  guysfree = guys[:]
  engaged  = {}
  men_pref2 = copy.deepcopy(men_pref)
  women_pref2 = copy.deepcopy(women_pref)
  while guysfree:
    guy = guysfree.pop(0)
    guyslist = men_pref2[guy]
    gal = guyslist.pop(0)
    fiance = engaged.get(gal)
    if not fiance:
      engaged[gal] = guy
      print("  %s and %s" % (guy, gal))
    else:
      galslist = women_pref2[gal]
      if galslist.index(fiance) > galslist.index(guy):
        engaged[gal] = guy
        print("  %s dumped %s for %s" % (gal, fiance, guy))
        if men_pref2[fiance]:
          guysfree.append(fiance)
      else:
        if guyslist:
          guysfree.append(guy)
  return engaged


print('\nEngagements:')
engaged = GSAlgo()

print('\nCouples:')
print('  ' + ',\n  '.join('%s is engaged to %s' % couple
                          for couple in sorted(engaged.items())))
print()
