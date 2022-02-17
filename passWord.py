"""
A game by, ClassicMC,
developed using the python programming lanugauge,
Made using just random stuff.
"""
import string, random, time
#Wait time before next words
def timeWait(waitTime):
    time.sleep(waitTime)
#Main game loop    
print("Loading...")
timeWait(0.5)
#Generates the main dictonaires 
tuff = ['sussy', 'chewey', 'messy', 'ugly',' terrible', 'passman','slimy','icky','glutten','thick','gay','slappy','elastic']    
tuff1 = ['bOy', 'maid','girlY', 'Thing', 'Profit', 'lazY', 'pyth0n','chair','mint','elephant','pen','cereal','nutCracker','r00ls','firePlace','cl0ck']    
tuff2 = ['0','1','2','3','4','5','6','7','8','9','10']
tuff3 = ['!','@','#','$','%','&',' ',' ',' '] 
finalPass = random.choice(tuff) + random.choice(tuff1) + random.choice(tuff2) + random.choice(tuff3)
print(finalPass)    
    
    