# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

engine1 = op('engine1')
engine2 = op('engine2')

def onOffToOn(channel, sampleIndex, val, prev):
	engine1.par.play = 1
	engine2.par.play = 1
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	current_index = parent.ToxSwitcher.par.Currentindex

	# turn off whatever engine is not being displayed
	if current_index == 0:
		engine2.par.play = 0
	elif current_index == 1:
		engine1.par.play = 0
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	return
	