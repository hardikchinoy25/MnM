

# Scenarios: Location, character, text, scene change, game state

# Scene 1    

def scene1(turn):
    scenario = [['california', 'maria', "You are 13 years old living in LA, California. You like styuding and reading comics. You are shy and do not have good friends.",'2','1']]
    return scenario[turn]

# Scene 2

def scene2(turn):
    scenario = [['school', '0', "Even at school, you are quiet. You often get bullied and feel lonely and isolated. ", '3', '1']]
    return scenario[turn]


# Scene 3

def scene3(turn):
    scenario = [['house','0',"After school, you always end up going home alone. You feel bad when you see children playing together but ignoring you.",'4','1']]
    return scenario[turn]


# Scene 4
def scene4(turn):
    scenario = [['room','0',"No one is home so you go upstairs and turn on your computer.",'5','1']]
    return scenario[turn]

# Scene 5
def scene5(turn):
    scenario = [['computer','0',"ooooooooooooooooooooooooooooooooooooo",'6','1']]
    return scenario[turn]
                 
# Scene 6
def scene6(turn):
    scenario = [['room','0',"You hurry and finish your homework, pack your bag with some comic books and leave. You see your mom is home.",'7','1']]
    return scenario[turn]
                 
# Scene 7
def scene7(turn):
    scenario = [['park','kidnapper',"You reach the park at 8 pm and don't see anyone from Westbridge there. In fact, it seems almost abandoned at this hour. ",'8','1']]
    return scenario[turn]