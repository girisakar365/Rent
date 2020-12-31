from random import choice,shuffle,randint
from db import db
class Password:

    def randomPassword():
        uniqueChar = ['!','@','#','$','&','-','_','.']
        capitalChar = [chr(65+i) for i in range(26)]
        normalChar = [chr(97+i) for i in range(26)]
        number = [str(i) for i in range(1,999)]

        def generatePassword():

            passwordGen = ''
            num = randint(8,12)
            choose=[uniqueChar,normalChar,number,capitalChar]
            for i in range(num):
                char = choice(choose)
                if len(passwordGen)<num:
                    passwordGen+=choice(char)
                else:
                    return passwordGen
                    break

        notNone= generatePassword()
        while notNone == None:
            notNone=generatePassword()
        else:
            return notNone

    def hexPassword(rawPassword,code='decode'):

        def decript():
            getit = rawPassword[rawPassword.find('<')+1:rawPassword.find('>')]
            store=''
            key = int(getit[getit.find(';')+1:])
            encripted='VIfDlQBPRb=1mu8LkUC0o@qO3jH7X!nEiW2$cw_tzKJ6e5s~Tv94SAG&p/.Y-Z^dgrNMFxa#hy|'
            for i in getit:
                store+=encripted[(encripted.find(i)-key)%len(encripted)]

            #Unpackgarbages
            key=store[store.find('~')+1:].split('&')
            del key[-1]
            value=store[0:store.find('~')]
            if len(key)!=len(value):
                del key[-1]
            #UnlockPattern
            patterndict={i:j for i,j in zip(key,value)}
            pattern=[int(i) for i in key]

            store=''
            pattern.sort()
            for i in pattern:
                store+=patterndict[str(i)]
            return store

        def encript():
            patterndict={i:j for i,j in enumerate(rawPassword)}

            key=list(patterndict.keys())
            value=list(patterndict.values())
            
            shuffle(key)#shuffle
            store=''
            pattern=''
            for i in key:#password+pattern
                store+=patterndict[i]
                pattern+='%s&'%str(i)
            rawpascode=store+'~'+pattern
            encripted='VIfDlQBPRb=1mu8LkUC0o@qO3jH7X!nEiW2$cw_tzKJ6e5s~Tv94SAG&p/.Y-Z^dgrNMFxa#hy|'
            store=''
            grab1=''
            grab2=''
            for i in range(5):
                grab1+=Password.randomPassword()
                grab2+=Password.randomPassword()
            key=randint(3,len(encripted))
            for i in rawpascode:
                store+=encripted[(encripted.find(i)+key)%len(encripted)]
            take=[ grab1+'<%s;%d>'%(store,key)+grab2,grab2+'<%s;%d>'%(store,key)+grab1]
            return choice(take)
        if code=='encode':
            return encript()
        else:
            return decript()

if db.cache('fetch','password')!='empty':
    encription = db.cache('fetch','password')
    decode = Password.hexPassword(encription,'decode')
    encode=Password.hexPassword(decode,'encode')
    db.cache('password',encode)