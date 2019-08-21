#To Do: Continue Game development

import os
import time

name=input('What is your name? ')
company=input('What company do you work for? ')
print('Automatic Restart enabled... Restarting now...')
time.sleep(7)
print('Restarting Auxillary Power...')
time.sleep(5)
print('Auxillary Power Offline... Retrying in 3 seconds')
time.sleep(3)
print('Restart Failed...')
time.sleep(5)
print('Restarting Secondary Power...')
time.sleep(2)
print('Secondary Power Online')
time.sleep(5)
print('Restarting Life Support...')
time.sleep(5)
print('Life Support Online')
time.sleep(2)
print('Restarting Communication...')
time.sleep(5)
print('Communication Offline... Retrying in 3 seconds')
time.sleep(3)
print('Restart Failed...')
time.sleep(1.5)
print('Restarting Navigation...')
time.sleep(4)
print('Navigation Minimal...')
time.sleep(3)
print('Restarting Emergency Beacon...')
time.sleep(2)

#GPS ACTIVATE
#MUST ACTIVATE TO CONTINUE

gps=input('To Restart Emergency Beacon, it requires GPS. Restart GPS? (Y/N) ')
if gps=='Y':
    print('Restarting GPS...')
    time.sleep(3)
    print('GPS Online')
    time.sleep(2)

elif gps=='N':
    print('GPS is required for Emergency Beacon. You are stranded and alone')


#VOICE ASSISTANT
#MUST AVTIVATE TO CONTINUE

voice=input('Would you like to restart voice assistant? (Y/N) ')
if voice=='Y':
    print('Restarting Voice Assistant...')
    time.sleep(6)
    print('Voice Assistant Online')
    time.sleep(3)

elif voice=='N':
    print('Voice Assistant helps you survive through the game. You dont know how to repair Communication and you are now stranded')
    





#SECONDARY FUNCTIONS
#MUST ACTIVATE TO CONTINUE
secondaryfunctions=input('Voice Assistant is trying to reroute Secondary Power to secondary functions. Would you like to block it? (Y/N) ')
if secondaryfunctions=='N':
    print('Restarting Internal Lights...')
    time.sleep(3)
    print('Internal Lights Online')
    time.sleep(1)
    print('Restarting Internal Storage...')
    time.sleep(3)
    print('Internal Storage Online')
    time.sleep(2.3)

elif secondaryfunctions=='Y':
    time.sleep(1)
    print('SYSTEM WARNING: Life Support will not be able to sustain life without Secondary Functions online. You Have suffocated')
    

printer=input('Assistant: ' + name + ' to recover communication we require a repair tool. Would you like to restart the 3D Printer? (Y/N)')
if printer=='Y':
    time.sleep(3)
    print('Restarting 3D printer...')
    print('3D Printer Online')

elif printer=='N':
    print('3D Printer is required to fix Communication. You are now stranded')

item=input('Assistant: ' + name + ' we only have enough recources to produce on item, would you like to print a repair tool or a stasis rifle? Type repair/stasis. ')
if item=='repair':
    print('Printer Progress: 10%')
    time.sleep(1)
    print('Printer Progress: 20%')
    time.sleep(1)
    print('Printer Progress: 30%')
    time.sleep(1)
    print('Printer Progress: 40%')
    time.sleep(1)
    print('Printer Progress: 50%')
    time.sleep(1)
    print('Printer Progress: 60%')
    time.sleep(1)
    print('Printer Progress: 70%')
    time.sleep(1)
    print('Printer Progress: 80%')
    time.sleep(1)
    print('Printer Progress: 90%')
    time.sleep(1)
    print('Printer Progress: 100%')
    time.sleep(1)
    print('Print Complete. Please collect')
    time.sleep(1)
    print('Assistent:' + name + ' please repair communications systems')
    time.sleep(3)
    print(name + ': Alright computer')
    time.sleep(1)
    print('Repair Progress: 10%')
    time.sleep(1)
    print('Repair Progress: 20%')
    time.sleep(1)
    print('Repair Progress: 30%')
    time.sleep(1)
    print('Repair Progress: 40%')
    time.sleep(1)
    print('Repair Progress: 50%')
    time.sleep(1)
    print('Repair Progress: 60%')
    time.sleep(1)
    print('Repair Progress: 70%')
    time.sleep(1)
    print('Repair Progress: 80%')
    time.sleep(1)
    print('Repair Progress: 90%')
    time.sleep(1)
    print('Repair Progress: 100%')
    time.sleep(2)
    print('Repair Complete')
    time.sleep(2)
    print('Restarting Communication...')
    time.sleep(3)
    print('Communication Online')
    time.sleep(2)
    print(name+ ': Computer contact ' + company )
    time.sleep(2)
    print('Assistant: Now contacting ' + company )
    time.sleep(1.5)
    print('+ company +: This is,' + company + ', We have recieved your distress call and a ship has been sent out to you. ETA: 127 days. Stay safe out there. ' + company + 'out.')

elif item=='stasis':
    print('Printer Progress: 10%')
    time.sleep(1)
    print('Printer Progress: 20%')
    time.sleep(1)
    print('Printer Progress: 30%')
    time.sleep(1)
    print('Printer Progress: 40%')
    time.sleep(1)
    print('Printer Progress: 50%')
    time.sleep(1)
    print('Printer Progress: 60%')
    time.sleep(1)
    print('Printer Progress: 70%')
    time.sleep(1)
    print('Printer Progress: 80%')
    time.sleep(1)
    print('Printer Progress: 90%')
    time.sleep(1)
    print('Printer Progress: 100%')
    time.sleep(1)
    print('Print Complete. Please collect')
    time.sleep(1)
    print('Assistant: WARNING, ' + name + 'there is a security alert. Entity appears to be a EUCLID class enemy. I recommend you take food, clean water and run. If the entity follows you, then use the stasis rifle.')
    time.sleep(3)
    print('You hear a loud scream. Slowly moving towards your direction.')
    time.sleep(1)
    print('Assistant: WARNING WARNING WARNING. EUCLID class entity approaching rappidly..')
    time.sleep(1)
    print('Assistant: WARNING HULL INTEGRETY AT 0%, EUCLID class entity has arrived.')
    time.sleep(1)
    print('The EUCLID class entity has destroyed your life-pod and has comletely swallowed you.')