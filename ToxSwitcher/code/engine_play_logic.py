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
	parent.ToxSwitcher.PlayBothEngines()
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	parent.ToxSwitcher.DisableNonDisplayedEngine()
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	return
	