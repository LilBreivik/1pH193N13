import random, sys
 
from backlogManager import BacklogManager

from flask import Flask

from keylinkassets import KeyLinkAssets

from Crypto.Cipher import AES

from subprocess import *

from colorama import init

init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected

from termcolor import cprint 

from pyfiglet import figlet_format 

def createNoise(bound=0, Noise="noisey"):

    # all possible chars that could be in the flag ..... 

    possibleLinks = KeyLinkAssets.createLinkAssets()

    possibleNoise = []
     
    for ctr in range(bound, 15):

        
        linkToAppend = random.randint(0, len(possibleLinks) -1)
        
        possibleNoise.extend(possibleLinks[linkToAppend])

    # to eliminate the chance, of creating two equal noises 

    createdNoise = ''.join(possibleNoise)

 

    if( Noise.__eq__(createdNoise)):

        createNoise(bound, createdNoise)

    
    return createdNoise


def createNoiseThatWillBePadded():


     # we need some input, to pad the 
    # AES Block Size 

     
    noise = ""

    neededBound = None

    possibleNoise = createNoise(0)

    lastBound = 42

    lastNoise = ""

    for bound  in range(16, 0, -1):

        possibleNoise = createNoise(bound)

        cipherTextLengthInBytes = int(simulateCTFChallenge(possibleNoise) / 8)   

        if cipherTextLengthInBytes  not in AES.key_size:

           # neededBound =  cipherTextLength 

            noise = lastNoise

            neededBound = lastBound

            BacklogManager.writeToBacklog("Needed Ciphertext-Length in Bytes " + str(lastBound ) )

            BacklogManager.writeToBacklog("We will stuff our recalculation with " + str(noise))

            sys.stdout.flush()
            break

        else: 

            lastNoise = possibleNoise
            lastBound = cipherTextLengthInBytes


    return ( noise, neededBound )

 


def createFlagCandidate():


    # all possible chars that could be in the flag ..... 

    possibleLinks = KeyLinkAssets.createLinkAssets()

    linkToAppend = random.randint(0, len(possibleLinks) -1)

    return linkToAppend





def simulateCTFChallenge(inputToTest):

    c = 'python3 turbocrypto.py' #Windows

    TestCandidate =  inputToTest + ' '

   
    handle = Popen(c, stdin=PIPE, stderr=PIPE, stdout=PIPE, shell=True)

    stdout_data = handle.communicate(input=TestCandidate.encode("utf-8"))[0]

    stdout_data=stdout_data.split("\n".encode("utf-8"))

    encryptedContentLength = 0


    # Debugging Purposes .... original ctf got just one BacklogManager.writeToBacklog !!! 

    for line in stdout_data:

        if len(line.decode()) > 0:

       #     BacklogManager.writeToBacklog("####Encrypted Content####")
        #    BacklogManager.writeToBacklog(line.decode())
         #   BacklogManager.writeToBacklog("####Encrypted Content####")

          #  BacklogManager.writeToBacklog("####Encrypted Content Length ####")
           # BacklogManager.writeToBacklog(len(line.decode()))
            encryptedContentLength = len(line.decode())

            #BacklogManager.writeToBacklog("####Encrypted Content Length ####")

    return encryptedContentLength





if __name__ == "__main__":

    BacklogManager.initLogger()
    cprint(figlet_format('1pH193N13!', font='alphabet'),
                          
       'yellow', 'on_red')
    
     # we need some input, to pad the 
    # AES Block Size 
 
    
    ( noise, neededBound ) = createNoiseThatWillBePadded()

    
    flagNotCracked = True

    candidateToTest = ""

    recalculatedFlag = ""

    possibleLinks = KeyLinkAssets.createLinkAssets()


    while(flagNotCracked):

         
        flagNotCracked = False

        for ctr in range(0, len(possibleLinks)):

            candidateToTest = possibleLinks[ctr]

            BacklogManager.writeToBacklog("candidateToTest " + candidateToTest)

            possiblePaddedFlag = noise + candidateToTest + recalculatedFlag
 

            cipherTextLengthInBytes = int(simulateCTFChallenge(possiblePaddedFlag) / 8)

            if neededBound == cipherTextLengthInBytes: 

                BacklogManager.writeToBacklog("###### candidate passed ######")
                BacklogManager.writeToBacklog("Recalculated Flag now : " + str(recalculatedFlag))
                BacklogManager.writeToBacklog("##########################") 
                

                recalculatedFlag = (candidateToTest + recalculatedFlag)

                flagNotCracked = True

            sys.stdout.flush()


    
    BacklogManager.writeToBacklog("###### flag recalculated ######")
    BacklogManager.writeToBacklog("Flag is : " + str(recalculatedFlag))
    BacklogManager.writeToBacklog("##########################") 

    sys.stdout.flush()

    cprint(figlet_format('Thx for using 1pH193N13!', font='alphabet'),
                          
       'yellow', 'on_red')

    
    

 