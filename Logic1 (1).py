#Note: This is an unfinished project. It is possible, for instance, to trick the logic_type_1 by using nonsenese statements. Almost everything only works for be verbs

string1= "All frogs are amphibians"
string2= "If something is a frog, then it is an amphibian"
string3= "If I was not late to work, then I did not commit the crime."
string4= "If I am right, then you should listen"
string5= "If something is a turtle, then it has a shell"
string6= "If the cats are not clawed, then they will not ruin the furniture"
string7= "All mammals are animals. All pigs are mammals. All pigs are animals."

def be_verb_finder_1(input1):
#Finds some of the be verbs
    try: 
        return input1.index(" is")
    except:
        try: 
            return input1.index(" are")
        except:
            try:
                return input1.index(" am")
            except:
                try:
                    return input1.index(" was")
                except:
                    try: 
                        input1.index(" were")
                    except:
                        pass

def frag1(input1):
#separates first fragment of string up until bverb
    return input1[0:be_verb_finder_1(input1)]

def frag2(input1):
#separates second fragment beginning at b verb
    return input1[be_verb_finder_1(input1)+1:len(input1)]

def antecedant_finder_1(input1):
#finds the antecedant in a conditional statement
    try: 
        return input1[0:input1.index(" then ")]
    except:
        pass

def consequent_finder_1(input1):
#finds the consequent in a conditional statement
    try: 
        return input1[input1.index("then "):len(input1)]
    except:
        pass

def subject_finder_1(input1):
#Finds the subject
    begsubject= frag1(input1).rindex(" ")
    return input1[begsubject+1:be_verb_finder_1(input1)]

def noun_after_finder1(input1):
#finds a nound that comes after a be verb
    list1= frag2(input1).split()
    if list1[1]=='not':
        return list1[2]
    else: 
        return list1[1]

def switcher_1(input1):
#Negates the consequent and turns it into the antecedent
    try:
        rep1=consequent_finder_1(input1).replace(" it "," "+subject_finder_1(antecedant_finder_1(input1))+" ").replace(" they "," "+subject_finder_1(antecedant_finder_1(input1))+" ")
        rep2=rep1.replace(" is "," is not ").replace(" are "," are not ").replace(" am "," am not ").replace(" was "," was not ").\
        replace(" were "," were not ").replace(" did "," did not ").replace(" should "," should not ").replace(" has "," does not have ")\
        .replace(" will "," will not ")
        rep3=rep2.replace("then ","If ")
        rep4=rep3.replace(" not not "," ")
        return rep4 + ", "
    except:
        pass

def switcher_2(input1):
#Negates the antecedant and turns it into the consequent
    try:
        rep1=antecedant_finder_1(input1).replace(" "+subject_finder_1(antecedant_finder_1(input1))+" "," it ")
        rep2=rep1.replace(" is "," is not ").replace(" are "," are not ").replace(" am "," am not ").replace(" was "," was not ")\
        .replace(" were "," were not ").replace(" did "," did not ").replace(" should "," should not ")\
        .replace(" has "," does not have ").replace(" will "," will not ")
        rep3=rep2.replace("If ","then ")
        rep4=rep3.replace(",",".")
        rep5=rep4.replace(" not not "," ")
        if subject_finder_1(antecedant_finder_1(input1))== "I":
            rep5= rep5.replace(" it "," I ")
        elif subject_finder_1(antecedant_finder_1(input1))== "we":
            rep5= rep5.replace(" it "," we ")
        elif subject_finder_1(antecedant_finder_1(input1))== "you":
            rep5= rep5.replace(" it "," you ")
        elif subject_finder_1(antecedant_finder_1(input1))== "they":
            rep5= rep5.replace(" it "," they ")
        elif str(subject_finder_1(antecedant_finder_1(input1))[::-1][0])=="s":
            rep5=rep5.replace(" it "," they ")
            rep5=rep5.replace(" the "," ")
        return rep5
    except:
        pass

def contrapositive_maker_1(input1):
#finds contrapositives (right now it only works if there is a be verb in the antecedant)
    contrapositivestring= str(switcher_1(input1))+str(switcher_2(input1))
    return contrapositivestring

logicsymbols1=['If','All ','All','Every','No','Some','then','if','all', 'every','no','not','some']
logicsymbols2=[' if ',' then ']

def logic_symbol_grabber_1(input1):
#picks out logic symbols but not repeats
    loglist1=input1.split()
    loglist3= list(filter(lambda i: i in loglist1, logicsymbols1))
    return loglist3

def onlyN(input1):
#Just gives numbers
    input_type= type(input1)
    return input_type().join(filter(input_type.isdigit, input1))

def logic_symbol_grabber_2(input1):
#converts logic symbols into a string of numbers
    rep1 = input1.replace('If ','0001')
    rep2= rep1.replace(' if ','0001')
    rep3= rep2.replace(' then ','0002')
    rep4= rep3.replace('All ','0003')
    rep5= rep4.replace(' all ','0003')
    rep6=rep5.replace('Every ', '0003')
    rep7=rep6.replace(' every ','0003')
    rep8=rep7.replace(' not ','0004')
    rep9=rep8.replace(' no ','0004')
    rep10=rep9.replace('No ','0004')
    rep11=rep10.replace('Some ','0005')
    rep12=rep11.replace(' some ','0005')
    rep13=rep12.replace(' therefore ','0006')
    rep14=rep13.replace(' therefore,','0006')
    rep15= onlyN(rep14)
    return rep15

def noun_organizer_1(input1):
#puts nouns in a list based on their positions around b verbs"""
    list1= input1[0:len(input1)-1].split(".")
    return [subject_finder_1(list1[0]), noun_after_finder1(list1[0]), subject_finder_1(list1[1]),\
    noun_after_finder1(list1[1]), subject_finder_1(list1[2]), noun_after_finder1(list1[2])]

def noun_pattern_1(input1):
# recognizes the pattern of nouns
    nounlist1= noun_organizer_1(input1)
    if nounlist1[0]==nounlist1[3] and nounlist1[1]==nounlist1[5] and nounlist1[2]==nounlist1[4]\
    and nounlist1[0] != nounlist1[1] and nounlist1[0] != nounlist1[2] and nounlist1[1] != nounlist1[2]:
        return 1
    elif nounlist1[0]==nounlist1[5] and nounlist1[1]==nounlist1[3] and nounlist1[2]==nounlist1[4]\
    and nounlist1[0] != nounlist1[1] and nounlist1[0] != nounlist1[2] and nounlist1[1] != nounlist1[2]:
        return 2
    elif nounlist1[0]==nounlist1[2] and nounlist1[1]==nounlist1[5] and nounlist1[3]==nounlist1[4]\
    and nounlist1[0] != nounlist1[1] and nounlist1[0] != nounlist1[3] and nounlist1[1] != nounlist1[3]:
        return 3
    elif nounlist1[0]==nounlist1[5] and nounlist1[1]==nounlist1[2] and nounlist1[3]==nounlist1[4]\
    and nounlist1[0] != nounlist1[1] and nounlist1[0] != nounlist1[3] and nounlist1[1] != nounlist1[3]:
        return 4
    else:
        pass

def logic_type_1(input1):
#describes that type of statement, argument, or syllogism a statement is. Doesn't analyze if terms carry
    rep1=str(logic_symbol_grabber_2(input1))
    if rep1== "00010002":
        return "Conditional Statement"
    elif rep1=="000100040002:":
        return "Conditional Statement"
    elif rep1=="000100020004":
        return "Conditional Statement"
    elif rep1=="0001000400020004":
        return "Conditional Statement"
    elif rep1=="000100020006":
        return "Modus Ponens"
    elif rep1=="00010002000400060004":
        return "Modus Tollens"
    elif rep1=="00030030003" and noun_pattern_1(input1)==1:
        return "Modus Barbara"
    elif rep1=="000400030004" and noun_pattern_1(input1)==1:
        return "Modus Celarent"
    elif rep1=="000300050005" and noun_pattern_1(input1)==1:
        return "Modus Darii"
    elif rep1=="0004000500050004" and noun_pattern_1(input1)==1:
        return "Modus Ferio"
    elif rep1=="000300030005" and noun_pattern_1(input1)==1:
        return "Modus Barbari"
    elif rep1=="0004000300050004" and noun_pattern_1(input1)==1:
        return "Modus Celaront"
    elif rep1=="000400030004" and noun_pattern_1(input1)==2:
        return "Modus Cesare"
    elif rep1=="000300040004" and noun_pattern_1(input1)==2:
        return "Modus Camestres"
    elif rep1=="0004000500050004" and noun_pattern_1(input1)==2:
        return "Modus Festino"
    elif rep1=="00030005000400050004" and noun_pattern_1(input1)==2:
        return "Baroco"
    elif rep1=="0004000300050004" and noun_pattern_1(input1)==2:
        return "Modus Cesaro"
    elif rep1=="00003000400050004" and noun_pattern_1(input1)==2:
        return "Modus Camestros"
    elif rep1=="000300050005" and noun_pattern_1(input1)==3:
        return "Modus Datisi"
    elif rep1=="000500030005" and noun_pattern_1(input1)==3:
        return "Modus Disamis"
    elif rep1=="0004000500050004" and noun_pattern_1(input1)==3:
        return "Modus Ferison"
    elif rep1=="00050004000300050004" and noun_pattern_1(input1)==3:
        return "Modus Bocardo"
    elif rep1=="0004000300050004" and noun_pattern_1(input1)==3:
        return "Modus Felapton"
    elif rep1=="000300030005" and noun_pattern_1(input1)==3:
        return "Modus Darapti"
    elif rep1=="000300040004" and noun_pattern_1(input1)==4:
        return "Modus Calemes"
    elif rep1=="000500030005" and noun_pattern_1(input1)==4:
        return "Modus Dimates"
    elif rep1=="0004000500050004" and noun_pattern_1(input1)==4:
        return "Modus Fresison"
    elif rep1=="0003000400050004" and noun_pattern_1(input1)==4:
        return "Modus Calemos"
    elif rep1=="0004000300050004" and noun_pattern_1(input1)==4:
        return "Modus Fesapo"
    elif rep1=="000300030005" and noun_pattern_1(input1)==4:
        return "Modus Bamalip"
    else:
        return "Can not determine"
    

list3 = list(filter(lambda i: i in logicsymbols1, logicsymbols2))

string8="If something is a dog, then it is a mammal. Hoppy is not mammal, therefore, Hoppy is not a dog"
string9="All dogs are mammals. No frogs are mammals. No frogs are dogs."


string10="No flowers are animals. All flowers are plants. Some plants are not animals."
string11="All pigs are vertebrates. Some farm animals are pigs. Some farm animals are vertebrates"

print (noun_organizer_1(string11))