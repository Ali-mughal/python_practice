
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#set flage 
active=True
responses={}
while active:
    name = input('whats your name:')
    opinion = input('whats your openion:')
    #get data in dic
    responses[name]=opinion
    active=input('do you want to give more opinion yes/no:')
    print(active)
    if active=='no':
        active=False
for name,opinion in responses.items():
    print('my name:'+name+'\n my opinion is:'+opinion)
