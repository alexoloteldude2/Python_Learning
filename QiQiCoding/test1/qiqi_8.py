#contacts= {'mom':'428759847','dad':'4587645986','child':'8476728'}
#for item in contacts.items() :
#    print(item[1])
#    print(item[0])
#ok
stationaries={'pencil':'$2','eraser':'$2','paper':'$1','pencil_case':'$20','toy_gun':'$60'}
stationaries['paper']='$0.2'
#Q1
del stationaries['toy_gun']
#Q2
stationaries['clay']='$8'
#Qbonus_question
for item in stationaries.items():
    print(item[0])
    print(item[1])
#Q3