#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.79.01), Wed Feb  5 02:11:45 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'igt'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[1280, 800], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instr"
instrClock = core.Clock()
image = visual.ImageStim(win=win, name='image',units='norm', 
    image='./image/inst.png', mask=None,
    ori=0, pos=[0,0], size=[2,2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()

Wait_com = visual.TextStim(win=win, ori=0, name='Wait_com',
    text='Wait Computer to Play',    font='Arial',
    units='norm', pos=[0, -0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

instr_th = u''

card_back_par = visual.ImageStim(win=win, name='card_back_par',units=u'norm', 
    image=u'./image/0.jpg', mask=None,
    ori=0, pos=[0, -0.35], size=[0.25, 0.55],
    color=[1,1,1], colorSpace=u'rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-6.0)
Wait_par = visual.TextStim(win=win, ori=0, name='Wait_par',
    text='Wait Participant to Play',    font='Arial',
    units='norm', pos=[0, -0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)
Please_Wait = visual.TextStim(win=win, ori=0, name='Please_Wait',
    text='Please Wait ...',    font='Arial',
    units='norm', pos=[0, -0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1.0,
    depth=-8.0)

card_back_com = visual.ImageStim(win=win, name='card_back_com',units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0, 0.3], size=[0.25, 0.55],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-10.0)
black_c = visual.ImageStim(win=win, name='black_c',units='norm', 
    image='./image/1.jpg', mask=None,
    ori=0, pos=[0,0], size=[0.25, 0.55],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-11.0)
red_c = visual.ImageStim(win=win, name='red_c',units='norm', 
    image='./image/2.jpg', mask=None,
    ori=0, pos=[0,0], size=[0.25, 0.55],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-12.0)
com_card_result = visual.ImageStim(win=win, name='com_card_result',units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0, 0.3], size=[0.25, 0.55],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-13.0)
par_card_result = visual.ImageStim(win=win, name='par_card_result',units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0, -0.35], size=[0.25, 0.55],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-14.0)
winorloss = visual.TextStim(win=win, ori=0, name='winorloss',
    text='nonsense',    font='Arial',
    units='norm', pos=[0, -0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-15.0)
Nochoice = visual.TextStim(win=win, ori=0, name='Nochoice',
    text='No choice was made',    font='Arial',
    units='norm', pos=[0, -0.4], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1.0,
    depth=-16.0)

top_card_n1 = visual.ImageStim(win=win, name='top_card_n1',units='norm', 
    image='sin', mask=None,
    ori=0, pos=[-0.5, 0.83], size=[0.14, 0.29],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-18.0)
top_card_n2 = visual.ImageStim(win=win, name='top_card_n2',units='norm', 
    image='sin', mask=None,
    ori=0, pos=[-0.25, 0.83], size=[0.14, 0.29],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-19.0)
top_card_n3 = visual.ImageStim(win=win, name='top_card_n3',units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0, 0.83], size=[0.14, 0.29],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-20.0)
top_card_n4 = visual.ImageStim(win=win, name='top_card_n4',units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0.25, 0.83], size=[0.14, 0.29],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-21.0)
top_card_n5 = visual.ImageStim(win=win, name='top_card_n5',units='norm', 
    image='sin', mask=None,
    ori=0, pos=[0.5, 0.83], size=[0.14, 0.29],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    texRes=128, interpolate=True, depth=-22.0)

# Initialize components for Routine "instr2"
instr2Clock = core.Clock()
instr2_thanks = visual.TextStim(win=win, ori=0, name='instr2_thanks',
    text='nonsense',    font='Arial',
    units='norm', pos=[0, 0], height=0.1, wrapWidth=1.4,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instr"-------
t = 0
instrClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
start_trial = event.BuilderKeyResponse()  # create an object of type KeyResponse
start_trial.status = NOT_STARTED
# keep track of which components have finished
instrComponents = []
instrComponents.append(image)
instrComponents.append(start_trial)
for thisComponent in instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if t >= 0.0 and image.status == NOT_STARTED:
        # keep track of start time/frame for later
        image.tStart = t  # underestimates by a little under one frame
        image.frameNStart = frameN  # exact frame index
        image.setAutoDraw(True)
    
    # *start_trial* updates
    if t >= 0 and start_trial.status == NOT_STARTED:
        # keep track of start time/frame for later
        start_trial.tStart = t  # underestimates by a little under one frame
        start_trial.frameNStart = frameN  # exact frame index
        start_trial.status = STARTED
        # keyboard checking is just starting
        start_trial.clock.reset()  # now t=0
        event.clearEvents()
    if start_trial.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        if len(theseKeys) > 0:  # at least one key was pressed
            start_trial.keys = theseKeys[-1]  # just the last key pressed
            start_trial.rt = start_trial.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
external_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('trial_loop.xlsx'),
    seed=None, name='external_loop')
thisExp.addLoop(external_loop)  # add the loop to the experiment
thisExternal_loop = external_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisExternal_loop.rgb)
if thisExternal_loop != None:
    for paramName in thisExternal_loop.keys():
        exec(paramName + '= thisExternal_loop.' + paramName)

for thisExternal_loop in external_loop:
    currentLoop = external_loop
    # abbreviate parameter names if possible (e.g. rgb = thisExternal_loop.rgb)
    if thisExternal_loop != None:
        for paramName in thisExternal_loop.keys():
            exec(paramName + '= thisExternal_loop.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    Sessions = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('trial_com_choices.xlsx'),
        seed=None, name='Sessions')
    thisExp.addLoop(Sessions)  # add the loop to the experiment
    thisSession = Sessions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisSession.rgb)
    if thisSession != None:
        for paramName in thisSession.keys():
            exec(paramName + '= thisSession.' + paramName)
    
    for thisSession in Sessions:
        currentLoop = Sessions
        # abbreviate parameter names if possible (e.g. rgb = thisSession.rgb)
        if thisSession != None:
            for paramName in thisSession.keys():
                exec(paramName + '= thisSession.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        parameter_mirror = 0
        import random
        card_box=list([1,2])
        rand_card=random.choice(card_box)
        if rand_card==1:
            targetPos1=[-0.7, 0]#on the left 
            targetPos2=[0.7, 0]#on the left
        else:
            targetPos1=[0.7, 0]#on the right
            targetPos2=[-0.7, 0]#on the left
        
        key_pressed = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_pressed.status = NOT_STARTED
        
        card_selected_com = 'fakevariable'
        if thisExternal_loop[u'sessionN'] == 's1':
          instr_th = u'You have finished session1, now you are going to session 2. \r\n\r\nWhen you are ready to start, press"SPACE"'
          if thisSession[u'com_result_pool'] == 1:
              com_result_image = './image/1.jpg'
              card_selected_com = 'Black card'
          if thisSession[u'com_result_pool'] == 2:
              com_result_image = './image/2.jpg'
              card_selected_com = 'Red card'
        
        if thisExternal_loop[u'sessionN'] == 's2':
          instr_th = u'Thanks'
          if thisSession[u'com_result_pool_s2'] == 1:
              com_result_image = './image/1.jpg'
              card_selected_com = 'Black card'
          if thisSession[u'com_result_pool_s2'] == 2:
              com_result_image = './image/2.jpg'
              card_selected_com = 'Red card'
        
        
        
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(Wait_com)
        trialComponents.append(key_pressed)
        trialComponents.append(card_back_par)
        trialComponents.append(Wait_par)
        trialComponents.append(Please_Wait)
        trialComponents.append(card_back_com)
        trialComponents.append(black_c)
        trialComponents.append(red_c)
        trialComponents.append(com_card_result)
        trialComponents.append(par_card_result)
        trialComponents.append(winorloss)
        trialComponents.append(Nochoice)
        trialComponents.append(top_card_n1)
        trialComponents.append(top_card_n2)
        trialComponents.append(top_card_n3)
        trialComponents.append(top_card_n4)
        trialComponents.append(top_card_n5)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *Wait_com* updates
            if t >= 0.0 and Wait_com.status == NOT_STARTED:
                # keep track of start time/frame for later
                Wait_com.tStart = t  # underestimates by a little under one frame
                Wait_com.frameNStart = frameN  # exact frame index
                Wait_com.setAutoDraw(True)
            elif Wait_com.status == STARTED and t >= (0.0 + 1.0):
                Wait_com.setAutoDraw(False)
            
            # *key_pressed* updates
            if t >= 1 and key_pressed.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_pressed.tStart = t  # underestimates by a little under one frame
                key_pressed.frameNStart = frameN  # exact frame index
                key_pressed.status = STARTED
                # keyboard checking is just starting
                key_pressed.clock.reset()  # now t=0
                event.clearEvents()
            elif key_pressed.status == STARTED and (t>=3 or len(key_pressed.keys)>0):
                key_pressed.status = STOPPED
            if key_pressed.status == STARTED:
                theseKeys = event.getKeys(keyList=['q', 'p'])
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_pressed.keys = theseKeys[-1]  # just the last key pressed
                    key_pressed.rt = key_pressed.clock.getTime()
                    parameter_mirror = 1
            card_selected = 'fakevariable'
            Choice_result = 'fakevariable'
            if len(key_pressed.keys)>0:
             opacity_par_back = 1
             opacity_please_wait = 1
             opacity_result = 1
             opacity_nochoice = 0
             mid_disap_time = key_pressed.rt + 0.5
             side_disap_time = 1 + key_pressed.rt + 0.5
             wait_par_time = key_pressed.rt
             if key_pressed.keys == 'q':
                if rand_card==1:
                    par_result_image = './image/1.jpg'
                    card_selected = 'Black card'
                if rand_card==2:
                    par_result_image = './image/2.jpg'
                    card_selected = 'Red card'
             if key_pressed.keys == 'p':
                if rand_card==1:
                    par_result_image = './image/2.jpg'
                    card_selected = 'Red card'
                if rand_card==2:
                    par_result_image = './image/1.jpg'
                    card_selected = 'Black card'
            
             if par_result_image == com_result_image:
              win_or_loss = 'You Win'
              Choice_result = 'Win'
             if par_result_image != com_result_image:
              win_or_loss = 'You Loss'
              Choice_result = 'Loss'
            
            
            if t >= 3 and len(key_pressed.keys)==0:
             parameter_mirror = 2
             opacity_par_back = 0
             opacity_please_wait = 0
             opacity_result = 0
             par_result_image = './image/1.jpg'
             opacity_nochoice = 1
             mid_disap_time = 2
             side_disap_time = 3
             wait_par_time = 2
             win_or_loss = 'You Loss'
             Choice_result = 'N/A'
             card_selected = 'N/A'
            
            
            Sessions.addData('com_choice', card_selected_com)
            Sessions.addData('sub_choice', card_selected)
            Sessions.addData('feedback', Choice_result)
            
            if thisSession[u'com_condi'] == 0:  # 1-5 are fake 
                          opacity_top_card_1 = 0
                          opacity_top_card_2 = 0
                          opacity_top_card_3 = 0
                          opacity_top_card_4 = 0
                          opacity_top_card_5 = 0
                          top_card_1 = './image/1.jpg' 
                          top_card_2 = './image/1.jpg'
                          top_card_3 = './image/2.jpg'
                          top_card_4 = './image/1.jpg'
                          top_card_5 = './image/2.jpg'
                    
            if thisSession[u'com_condi'] == 1: # 2-5 are fake 
                          opacity_top_card_1 = 1
                          opacity_top_card_2 = 0
                          opacity_top_card_3 = 0
                          opacity_top_card_4 = 0
                          opacity_top_card_5 = 0
                          top_card_2 = './image/1.jpg'
                          top_card_3 = './image/2.jpg'
                          top_card_4 = './image/1.jpg'
                          top_card_5 = './image/2.jpg'
                          if thisExternal_loop[u'sessionN'] == 's1':
                             top_card_1 = './image/2.jpg' # real one
                          if thisExternal_loop[u'sessionN'] == 's2':
                             top_card_1 = './image/1.jpg' 
            
                        
            if thisSession[u'com_condi'] == 2:
                          opacity_top_card_1 = 1
                          opacity_top_card_2 = 1
                          opacity_top_card_3 = 0
                          opacity_top_card_4 = 0
                          opacity_top_card_5 = 0
                          top_card_3 = './image/2.jpg'
                          top_card_4 = './image/1.jpg'
                          top_card_5 = './image/2.jpg'
                          if thisExternal_loop[u'sessionN'] == 's1':
                             top_card_1 = './image/2.jpg'# real one
                             top_card_2 = './image/1.jpg'# real one
                          if thisExternal_loop[u'sessionN'] == 's2':
                             top_card_1 = './image/1.jpg'
                             top_card_2 = './image/2.jpg'
            
            if thisSession[u'com_condi'] == 3:
                          opacity_top_card_1 = 1
                          opacity_top_card_2 = 1
                          opacity_top_card_3 = 1
                          opacity_top_card_4 = 0
                          opacity_top_card_5 = 0
                          top_card_4 = './image/1.jpg'
                          top_card_5 = './image/2.jpg'
                          if thisExternal_loop[u'sessionN'] == 's1':
                             top_card_1 = './image/2.jpg'# real one
                             top_card_2 = './image/1.jpg'# real one
                             top_card_3 = './image/1.jpg'# real one
                          if thisExternal_loop[u'sessionN'] == 's2':
                             top_card_1 = './image/1.jpg'# real one
                             top_card_2 = './image/2.jpg'# real one
                             top_card_3 = './image/2.jpg'# real one
            
                        
            if thisSession[u'com_condi'] == 4:
                          opacity_top_card_1 = 1
                          opacity_top_card_2 = 1
                          opacity_top_card_3 = 1
                          opacity_top_card_4 = 1
                          opacity_top_card_5 = 0
                          top_card_5 = './image/2.jpg'
                          if thisExternal_loop[u'sessionN'] == 's1':
                             top_card_1 = './image/2.jpg'# real one
                             top_card_2 = './image/1.jpg'# real one
                             top_card_3 = './image/1.jpg'# real one
                             top_card_4 = './image/2.jpg'# real one
                          if thisExternal_loop[u'sessionN'] == 's2':
                             top_card_1 = './image/1.jpg'# real one
                             top_card_2 = './image/2.jpg'# real one
                             top_card_3 = './image/2.jpg'# real one
                             top_card_4 = './image/1.jpg'# real one
            
                        
            if thisSession[u'com_condi'] == 5:
                          opacity_top_card_1 = 1
                          opacity_top_card_2 = 1
                          opacity_top_card_3 = 1
                          opacity_top_card_4 = 1
                          opacity_top_card_5 = 1
                          if thisExternal_loop[u'sessionN'] == 's1':
                             top_card_1 = './image/2.jpg'# real one
                             top_card_2 = './image/1.jpg'# real one
                             top_card_3 = './image/1.jpg'# real one
                             top_card_4 = './image/2.jpg'# real one
                             top_card_5 = './image/1.jpg'# real one
                          if thisExternal_loop[u'sessionN'] == 's2':
                             top_card_1 = './image/1.jpg'# real one
                             top_card_2 = './image/2.jpg'# real one
                             top_card_3 = './image/2.jpg'# real one
                             top_card_4 = './image/1.jpg'# real one
                             top_card_5 = './image/2.jpg'# real one
                        
            if thisSession[u'com_condi'] > 5:
                    prevTrial_5 = Sessions.getEarlierTrial(-5) 
                    prevTrial_4 = Sessions.getEarlierTrial(-4) 
                    prevTrial_3 = Sessions.getEarlierTrial(-3) 
                    prevTrial_2 = Sessions.getEarlierTrial(-2) 
                    prevTrial_1 = Sessions.getEarlierTrial(-1) 
                    opacity_top_card_1 = 1
                    opacity_top_card_2 = 1
                    opacity_top_card_3 = 1
                    opacity_top_card_4 = 1
                    opacity_top_card_5 = 1
                    if thisExternal_loop[u'sessionN'] == 's1':
                          if prevTrial_5[u'com_result_pool'] == 1:
                             top_card_1 = './image/1.jpg'
                          if prevTrial_5[u'com_result_pool'] == 2:
                             top_card_1 = './image/2.jpg'
            
                          if prevTrial_4[u'com_result_pool'] == 1:
                             top_card_2 = './image/1.jpg'
                          if prevTrial_4[u'com_result_pool'] == 2:
                             top_card_2 = './image/2.jpg'
            
                          if prevTrial_3[u'com_result_pool'] == 1:
                             top_card_3 = './image/1.jpg'
                          if prevTrial_3[u'com_result_pool'] == 2:
                             top_card_3 = './image/2.jpg'
            
                          if prevTrial_2[u'com_result_pool'] == 1:
                             top_card_4 = './image/1.jpg'
                          if prevTrial_2[u'com_result_pool'] == 2:
                             top_card_4 = './image/2.jpg'
            
                          if prevTrial_1[u'com_result_pool'] == 1:
                             top_card_5 = './image/1.jpg'
                          if prevTrial_1[u'com_result_pool'] == 2:
                             top_card_5 = './image/2.jpg'
            
                    if thisExternal_loop[u'sessionN'] == 's2':
                          if prevTrial_5[u'com_result_pool_s2'] == 1:
                             top_card_1 = './image/1.jpg'
                          if prevTrial_5[u'com_result_pool_s2'] == 2:
                             top_card_1 = './image/2.jpg'
            
                          if prevTrial_4[u'com_result_pool_s2'] == 1:
                             top_card_2 = './image/1.jpg'
                          if prevTrial_4[u'com_result_pool_s2'] == 2:
                             top_card_2 = './image/2.jpg'
            
                          if prevTrial_3[u'com_result_pool_s2'] == 1:
                             top_card_3 = './image/1.jpg'
                          if prevTrial_3[u'com_result_pool_s2'] == 2:
                             top_card_3 = './image/2.jpg'
            
                          if prevTrial_2[u'com_result_pool_s2'] == 1:
                             top_card_4 = './image/1.jpg'
                          if prevTrial_2[u'com_result_pool_s2'] == 2:
                             top_card_4 = './image/2.jpg'
            
                          if prevTrial_1[u'com_result_pool_s2'] == 1:
                             top_card_5 = './image/1.jpg'
                          if prevTrial_1[u'com_result_pool_s2'] == 2:
                             top_card_5 = './image/2.jpg'
            
            
            # *card_back_par* updates
            if (len(key_pressed.keys)>0 or parameter_mirror == 2) and card_back_par.status == NOT_STARTED:
                # keep track of start time/frame for later
                card_back_par.tStart = t  # underestimates by a little under one frame
                card_back_par.frameNStart = frameN  # exact frame index
                card_back_par.setAutoDraw(True)
            elif card_back_par.status == STARTED and t >= (card_back_par.tStart + 0.5):
                card_back_par.setAutoDraw(False)
            if card_back_par.status == STARTED:  # only update if being drawn
                card_back_par.setOpacity(opacity_par_back, log=False)
            
            # *Wait_par* updates
            if t >= 1 and Wait_par.status == NOT_STARTED:
                # keep track of start time/frame for later
                Wait_par.tStart = t  # underestimates by a little under one frame
                Wait_par.frameNStart = frameN  # exact frame index
                Wait_par.setAutoDraw(True)
            elif Wait_par.status == STARTED and (len(key_pressed.keys)>0 or parameter_mirror == 2):
                Wait_par.setAutoDraw(False)
            
            # *Please_Wait* updates
            if (len(key_pressed.keys)>0 or parameter_mirror == 2) and Please_Wait.status == NOT_STARTED:
                # keep track of start time/frame for later
                Please_Wait.tStart = t  # underestimates by a little under one frame
                Please_Wait.frameNStart = frameN  # exact frame index
                Please_Wait.setAutoDraw(True)
            elif Please_Wait.status == STARTED and ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2):
                Please_Wait.setAutoDraw(False)
            if Please_Wait.status == STARTED:  # only update if being drawn
                Please_Wait.setOpacity(opacity_please_wait, log=False)
                Please_Wait.setText(Please_Wait.text, log=False)
            
            # *card_back_com* updates
            if t >= 1 and card_back_com.status == NOT_STARTED:
                # keep track of start time/frame for later
                card_back_com.tStart = t  # underestimates by a little under one frame
                card_back_com.frameNStart = frameN  # exact frame index
                card_back_com.setAutoDraw(True)
            elif card_back_com.status == STARTED and ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2):
                card_back_com.setAutoDraw(False)
            if card_back_com.status == STARTED:  # only update if being drawn
                card_back_com.setImage('./image/0.jpg', log=False)
            
            # *black_c* updates
            if t >= 0 and black_c.status == NOT_STARTED:
                # keep track of start time/frame for later
                black_c.tStart = t  # underestimates by a little under one frame
                black_c.frameNStart = frameN  # exact frame index
                black_c.setAutoDraw(True)
            elif black_c.status == STARTED and ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2):
                black_c.setAutoDraw(False)
            if black_c.status == STARTED:  # only update if being drawn
                black_c.setPos(targetPos1, log=False)
            
            # *red_c* updates
            if t >= 0.0 and red_c.status == NOT_STARTED:
                # keep track of start time/frame for later
                red_c.tStart = t  # underestimates by a little under one frame
                red_c.frameNStart = frameN  # exact frame index
                red_c.setAutoDraw(True)
            elif red_c.status == STARTED and ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2):
                red_c.setAutoDraw(False)
            if red_c.status == STARTED:  # only update if being drawn
                red_c.setPos(targetPos2, log=False)
            
            # *com_card_result* updates
            if ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2) and com_card_result.status == NOT_STARTED:
                # keep track of start time/frame for later
                com_card_result.tStart = t  # underestimates by a little under one frame
                com_card_result.frameNStart = frameN  # exact frame index
                com_card_result.setAutoDraw(True)
            elif com_card_result.status == STARTED and t >= (com_card_result.tStart + 1):
                com_card_result.setAutoDraw(False)
            if com_card_result.status == STARTED:  # only update if being drawn
                com_card_result.setImage(com_result_image, log=False)
            
            # *par_card_result* updates
            if ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2) and par_card_result.status == NOT_STARTED:
                # keep track of start time/frame for later
                par_card_result.tStart = t  # underestimates by a little under one frame
                par_card_result.frameNStart = frameN  # exact frame index
                par_card_result.setAutoDraw(True)
            elif par_card_result.status == STARTED and t >= (par_card_result.tStart + 1.0):
                par_card_result.setAutoDraw(False)
            if par_card_result.status == STARTED:  # only update if being drawn
                par_card_result.setOpacity(opacity_result, log=False)
                par_card_result.setImage(par_result_image, log=False)
            
            # *winorloss* updates
            if ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2) and winorloss.status == NOT_STARTED:
                # keep track of start time/frame for later
                winorloss.tStart = t  # underestimates by a little under one frame
                winorloss.frameNStart = frameN  # exact frame index
                winorloss.setAutoDraw(True)
            elif winorloss.status == STARTED and t >= (winorloss.tStart + 1.0):
                winorloss.setAutoDraw(False)
            if winorloss.status == STARTED:  # only update if being drawn
                winorloss.setText(win_or_loss, log=False)
            
            # *Nochoice* updates
            if ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2) and Nochoice.status == NOT_STARTED:
                # keep track of start time/frame for later
                Nochoice.tStart = t  # underestimates by a little under one frame
                Nochoice.frameNStart = frameN  # exact frame index
                Nochoice.setAutoDraw(True)
            elif Nochoice.status == STARTED and t >= (Nochoice.tStart + 1.0):
                Nochoice.setAutoDraw(False)
            if Nochoice.status == STARTED:  # only update if being drawn
                Nochoice.setOpacity(opacity_nochoice, log=False)
                Nochoice.setText(Nochoice.text, log=False)
            
            # *top_card_n1* updates
            if t >= 0.0 and top_card_n1.status == NOT_STARTED:
                # keep track of start time/frame for later
                top_card_n1.tStart = t  # underestimates by a little under one frame
                top_card_n1.frameNStart = frameN  # exact frame index
                top_card_n1.setAutoDraw(True)
            elif top_card_n1.status == STARTED and ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2):
                top_card_n1.setAutoDraw(False)
            if top_card_n1.status == STARTED:  # only update if being drawn
                top_card_n1.setOpacity(opacity_top_card_1, log=False)
                top_card_n1.setImage(top_card_1, log=False)
            
            # *top_card_n2* updates
            if t >= 0.0 and top_card_n2.status == NOT_STARTED:
                # keep track of start time/frame for later
                top_card_n2.tStart = t  # underestimates by a little under one frame
                top_card_n2.frameNStart = frameN  # exact frame index
                top_card_n2.setAutoDraw(True)
            elif top_card_n2.status == STARTED and ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2):
                top_card_n2.setAutoDraw(False)
            if top_card_n2.status == STARTED:  # only update if being drawn
                top_card_n2.setOpacity(opacity_top_card_2, log=False)
                top_card_n2.setImage(top_card_2, log=False)
            
            # *top_card_n3* updates
            if t >= 0.0 and top_card_n3.status == NOT_STARTED:
                # keep track of start time/frame for later
                top_card_n3.tStart = t  # underestimates by a little under one frame
                top_card_n3.frameNStart = frameN  # exact frame index
                top_card_n3.setAutoDraw(True)
            elif top_card_n3.status == STARTED and ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2):
                top_card_n3.setAutoDraw(False)
            if top_card_n3.status == STARTED:  # only update if being drawn
                top_card_n3.setOpacity(opacity_top_card_3, log=False)
                top_card_n3.setImage(top_card_3, log=False)
            
            # *top_card_n4* updates
            if t >= 0.0 and top_card_n4.status == NOT_STARTED:
                # keep track of start time/frame for later
                top_card_n4.tStart = t  # underestimates by a little under one frame
                top_card_n4.frameNStart = frameN  # exact frame index
                top_card_n4.setAutoDraw(True)
            elif top_card_n4.status == STARTED and ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2):
                top_card_n4.setAutoDraw(False)
            if top_card_n4.status == STARTED:  # only update if being drawn
                top_card_n4.setOpacity(opacity_top_card_4, log=False)
                top_card_n4.setImage(top_card_4, log=False)
            
            # *top_card_n5* updates
            if t >= 0.0 and top_card_n5.status == NOT_STARTED:
                # keep track of start time/frame for later
                top_card_n5.tStart = t  # underestimates by a little under one frame
                top_card_n5.frameNStart = frameN  # exact frame index
                top_card_n5.setAutoDraw(True)
            elif top_card_n5.status == STARTED and ((parameter_mirror == 1 and t > 1+ key_pressed.rt + 0.5) or parameter_mirror == 2):
                top_card_n5.setAutoDraw(False)
            if top_card_n5.status == STARTED:  # only update if being drawn
                top_card_n5.setOpacity(opacity_top_card_5, log=False)
                top_card_n5.setImage(top_card_5, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if key_pressed.keys in ['', [], None]:  # No response was made
           key_pressed.keys=None
        # store data for Sessions (TrialHandler)
        Sessions.addData('key_pressed.keys',key_pressed.keys)
        if key_pressed.keys != None:  # we had a response
            Sessions.addData('key_pressed.rt', key_pressed.rt)
        
        
        
        
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Sessions'
    
    # get names of stimulus parameters
    if Sessions.trialList in ([], [None], None):  params = []
    else:  params = Sessions.trialList[0].keys()
    # save data for this loop
    Sessions.saveAsExcel(filename + '.xlsx', sheetName='Sessions',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    Sessions.saveAsText(filename + 'Sessions.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    #------Prepare to start Routine "instr2"-------
    t = 0
    instr2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_continue = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_continue.status = NOT_STARTED
    # keep track of which components have finished
    instr2Components = []
    instr2Components.append(instr2_thanks)
    instr2Components.append(key_continue)
    for thisComponent in instr2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instr2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instr2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr2_thanks* updates
        if t >= 0.0 and instr2_thanks.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr2_thanks.tStart = t  # underestimates by a little under one frame
            instr2_thanks.frameNStart = frameN  # exact frame index
            instr2_thanks.setAutoDraw(True)
        if instr2_thanks.status == STARTED:  # only update if being drawn
            instr2_thanks.setText(instr_th, log=False)
        
        # *key_continue* updates
        if t >= 0.0 and key_continue.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_continue.tStart = t  # underestimates by a little under one frame
            key_continue.frameNStart = frameN  # exact frame index
            key_continue.status = STARTED
            # keyboard checking is just starting
            event.clearEvents()
        if key_continue.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "instr2"-------
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'external_loop'

# get names of stimulus parameters
if external_loop.trialList in ([], [None], None):  params = []
else:  params = external_loop.trialList[0].keys()
# save data for this loop
external_loop.saveAsExcel(filename + '.xlsx', sheetName='external_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
external_loop.saveAsText(filename + 'external_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])






win.close()
core.quit()
