import random

#Parameters
 #Defined by protocol
votingwindow=10000
 #Averaging window
window=1000
 # what % of voters are apathetic?
apathetic=.8
 # what % of non-apathetic voters consent to this motion?
consent=0.2
 # how many 'yes' blocks in a row to start?  (you can make your own initial array further down in the code if you want)
initial=1000
 # how many data points after initialization?
iterations=100000

#Random function
def rand(weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i

#Determining the Next Vote
prob=[]
def nextvote(votelist,window,votingwindow,apathetic,consent):
    autoconsent=float(sum(votelist[windowloc:]))/window
    totalconsent=autoconsent*apathetic + consent*(1-apathetic)
    vote=rand([1-totalconsent,totalconsent])
    global prob
    prob.append(totalconsent)
    votelist.append(vote)
    del votelist[0]
    return votelist

#Initiating the voting history
votelist=[0]*votingwindow
beginloc=votingwindow-initial
windowloc=votingwindow-window
votelist[beginloc:]=[1]*initial

#Go!
passed=False
voting=[]
for i in range(1,iterations):
    votelist=nextvote(votelist,window,votingwindow,apathetic,consent)
    valid=float(sum(votelist))/votingwindow
    voting.append(valid)
    if valid >= 0.5:
        passed=True
        
#Finish Up
print 'passed?',passed
index=list(range(1,iterations))
with open("frequencyvoting.txt", "a") as myfile:
    for j in range(0,iterations-1):
           print>>myfile, str(index[j])+' '+str(prob[j])+' '+str(voting[j])
