import random
import math
from Crypto.Hash import SHA3_224


#nonce = random.getrandbits(128)
#print(nonce)
nonce=31892260


nonce1=str(nonce).zfill(32)

h_amt = SHA3_224.new()
h_amt.update(b'4933601832480809353473354884041175248572605852782963066896748056885475641656749621629491905191014868618662270686970232166446509470324736864650682101529030248099045013028061692922691724625514706329230172429768068340125863618218559912413117007754845075429408372888507551698514494498492001013849289727206925716097505112821640035328796287477288832274302228451772267834762720729040136679341742771582480873438819854901251010698577442809438919694733749250049741106149694027735988626092669792535204681665271762659664614542674529824442558625688825977054069126171946431554677605767056236181410658731273842816008767266250489001')

m1=(int(h_amt.hexdigest(),16))
print (m1)
m2=97505112821640035328796287477288832274302228451772267834762720729040136679341742771582480873438819854901251010698577442809438919694733749250049741106149694027735988626092669792535204681665271762659664614542674529824442558625688825977054069126171946431554677605767056236181410658731273842816008767266250489001280169915740075275463861503071077827418510488421690725013474318539523766137805810211274253119265266794062657346520380297929446776964680840753792271484649603844540374503251217107197349531253543136676535714181314196638094634788652360665349380808183893389246792041278361500353029057939049744097435458534763893701
T1=str(m1)+str(m2)+str(nonce1)
print(T1)
h_T1 = SHA3_224.new()
h_T1.update(T1.encode('utf-16'))
print(h_T1.hexdigest())

while int(h_T1.hexdigest(),16)>= 0x000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:
     nonce+=1  # Increment nonce (ie change your guess)
     nonce1 = str(nonce).zfill(31)
     T1 = str(m1) + str(m2) + str(nonce1)
     h_T1 = SHA3_224.new()
     h_T1.update(T1.encode('utf-16'))

     print('Nonce Guess: ', nonce)
     print('Resultant Hash: ' , (h_T1.hexdigest()))

if (int(h_T1.hexdigest(),16)== 0x000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF):
    print('Resultant Hash: ' , (h_T1.hexdigest()))

    print('success')





