#load modules
from psychopy import visual, event, core, gui
import glob #fetch all file names from a folder 
import random #to randomize 
import pandas as pd #give it a shorter name that we can refer to later on 
import numpy as np
import string


#experiment
#define pop-up to request participant info before the experiment starts
popup = gui.Dlg(title = "Påske-spil") #give it a title
popup.addField("ID:")  
popup.addField("Alder:")
popup.addField("Køn:", choices = ["kvinde", "mand", "andet"]) #choices make a dropdown menu 


#show dialogue box as a pop-up
popup.show()

#define main window
win = visual.Window(fullscr = True, color = "black") #define fullscreen and color inside the window


#get the data from the pop-up box
if popup.OK:
    ID = popup.data[0] #use the indexes to refer
    Age = popup.data[1]
    Gender = popup.data[2]
elif popup.Cancel:
    core.quit() #possibility of cancelling



#define our priming word in a list, then randomize which one is picked
priming_word_brev = ["på bordet", "på gulvet"]
random.shuffle(priming_word_brev)

priming_word_kors = ["kirkegården", "gravpladsen"]
random.shuffle(priming_word_kors)

priming_word_choko = ["mængden", "alt"]
random.shuffle(priming_word_choko)

priming_word_kyl = ["på kyllingefarmen", "i gruppen"]
random.shuffle(priming_word_kyl)

priming_word_mal = ["lagt ud", "i massen"]
random.shuffle(priming_word_mal)

priming_word_harer = ["snedriven", "snelandskabet"]
random.shuffle(priming_word_harer)

#define the texts with curly brackets {} for our priming words which will be inserted with the .format()
question = visual.TextStim(win, text = "sample {} sample?".format(priming_word_kors[0]))


#get a list of stimulus file names
stimuli = glob.glob("stimuli_easter/IMG*") #whatever file which name starts with stimulus is put into a list

#randomize order of stimuli everytime the script is run
random.shuffle(stimuli)

print(stimuli)

#define stop watch
stopwatch = core.Clock()

#define logfile dataframe
DATA = pd.DataFrame(columns = ["ID", "Age", "Gender", "Stimuli", "Condition_kyl", "Condition_choko", "Condition_kors", "Condition_brev", "Condition_mal", "Condition_harer", "Response"])

#texts in the experiment 
msg_start = visual.TextStim(win, text = "Velkommen til dette påske-eksperiment! Om et øjeblik vil du se en række påske-billeder, der kun vises kortvarigt. Du skal forsøge at vurdere, hvor mange påske-ting, der forekommer på hvert billede. Tryk på en hvilken som helst tast, når du er klar til at fortsætte.")
msg_start_2 = visual.TextStim(win, text = "Hold øjnene på skærmen! Det første påske-billede vil vises, når du trykker på en hvilken som helst tast på tastaturet.")
msg_end = visual.TextStim(win, text = "Påske-eksperimentet er nu slut! Lod du mon dine estimater påvirke af ordvalget?")
CapturedResponseString = visual.TextStim(win, units='norm', height = 0.075, wrapWidth = 1.6, text='', color = 'white', pos = (0,-0.6))
captured_string = ''
    

def updateTheResponse(captured_string):
    CapturedResponseString.setText(captured_string)
    question.draw()
    CapturedResponseString.draw()
    win.flip()
        




#show start
msg_start.draw()
win.flip()
event.waitKeys() #any key can be pressed

#show start 2
msg_start_2.draw()
win.flip()
event.waitKeys() #any key can be pressed


#make our loop
for i in stimuli: #for every stimuli (i)
    img = visual.ImageStim(win, i) #present image
    img.draw() #draw
    win.flip() #flip
    core.wait(0.4) 
    if i == 'stimuli_easter\\IMG_2319.JPG':
        question.text = "Hvor mange gækkebreve tror du, at der var {}? Angiv dit svar i hele tal. Tallene vil kunne ses på skærmen, når du begynder at skrive. Tryk på 'Enter', når du har skrevet dit svar og er klar til at fortsætte.".format(priming_word_brev[0])
            
    elif i == 'stimuli_easter\\IMG_2320.jpg':
        question.text = "Hvor mange kors tror du, at {} havde? Angiv dit svar i hele tal. Tallene vil kunne ses på skærmen, når du begynder at skrive. Tryk på 'Enter', når du har skrevet dit svar og er klar til at fortsætte.".format(priming_word_kors[0])
        
    elif i == 'stimuli_easter\\IMG_2321.JPG':
        question.text = "Hvor mange chokoladeæg tror du, at der var i {}? Angiv dit svar i hele tal. Tallene vil kunne ses på skærmen, når du begynder at skrive. Tryk på 'Enter', når du har skrevet dit svar og er klar til at fortsætte.".format(priming_word_choko[0])
        
    elif i == 'stimuli_easter\\IMG_2322.JPG':
        question.text = "Hvor mange påskekyllinger tror du, at der var {}? Angiv dit svar i hele tal. Tallene vil kunne ses på skærmen, når du begynder at skrive. Tryk på 'Enter', når du har skrevet dit svar og er klar til at fortsætte.".format(priming_word_kyl[0])
        
    elif i == 'stimuli_easter\\IMG_2323.JPG':
        question.text = "Hvor mange malede æg tror du, at der var {}? Angiv dit svar i hele tal. Tallene vil kunne ses på skærmen, når du begynder at skrive. Tryk på 'Enter', når du har skrevet dit svar og er klar til at fortsætte.".format(priming_word_mal[0])
        
    elif i == 'stimuli_easter\\IMG_2324.JPG':
        question.text = "Hvor mange påskeharer tror du, at der var i {}? Angiv dit svar i hele tal. Tallene vil kunne ses på skærmen, når du begynder at skrive. Tryk på 'Enter', når du har skrevet dit svar og er klar til at fortsætte.".format(priming_word_harer[0])
        
    updateTheResponse(captured_string)
    
    subject_response_finished = False # only changes when they hit return
    while not subject_response_finished:
        for key in event.getKeys(keyList = ["0","1","2", "3", "4", "5", "6", "7", "8", "9", "escape", "backspace", "return"]):
            if key in ['return']:
                #print 'participant typed %s' %captured_string
                response = captured_string
                captured_string = ''
                subject_response_finished = True
            
            elif key in ['escape']:
                core.quit()
                
            #allow the participant to do deletions too , using the 
            # delete key, and show the change they made
            elif key in ['delete','backspace']:
                captured_string = captured_string[:-1] #delete last character
                updateTheResponse(captured_string)
            #handle spaces
            elif key in ['space']:
                captured_string = captured_string+' '
                updateTheResponse(captured_string)
            elif key in ['period']:
                captured_string = captured_string+'.'
                updateTheResponse(captured_string)
            elif key in ['comma']:
                captured_string = captured_string+','
                updateTheResponse(captured_string)
            elif key in ['lshift','rshift']:
                pass #do nothing when some keys are pressed
            #if any other key is pressed, add it to the string and 
            # show the participant what they typed
            else: 
                captured_string = captured_string+key
                #show it
                updateTheResponse(captured_string)
    
    DATA = DATA.append({
            "ID":ID,
            "Age": Age,
            "Gender": Gender,
            "Stimuli": i, 
            "Condition_choko": priming_word_choko[0],
            "Condition_kors": priming_word_kors[0],
            "Condition_mal": priming_word_mal[0],
            "Condition_brev": priming_word_brev[0],
            "Condition_kyl": priming_word_kyl[0],
            "Condition_harer": priming_word_harer[0],
            "Response": response}, ignore_index = True) 
            




#show end text
msg_end.draw()
win.flip()
core.wait(5) #last for 5 seconds


#save the logfile 
logfile_name = "easter_logfiles/logfile_{}.csv".format(ID) #puts the ID of the participant into the name of the file 
DATA.to_csv(logfile_name)
