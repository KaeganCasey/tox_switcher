"""
Extension classes enhance TouchDesigner components with python. An
extension is accessed via ext.ExtensionClassName from any operator
within the extended component. If the extension is promoted via its
Promote Extension parameter, all its attributes with capitalized names
can be accessed externally, e.g. op('yourComp').PromotedFunction().

Help: search "Extensions" in wiki
"""

from TDStoreTools import StorageManager
import TDFunctions as TDF

class ToxSwitcherEXT:
	"""
	ToxSwitcherEXT description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

		# internal op shortcuts to engine comps
		self.engine1 = op('engine1')
		self.engine2 = op('engine2')

	def PlayEngine(self, engine_num: int, play: bool = True) -> None:
		"""Play either of the engines referring to them using #'s zero or one.
		"""
		if engine_num == 0:
			self.engine1.par.play = play
		elif engine_num == 1:
			self.engine2.par.play = play
		else:
			raise ValueError('Engine number out of bounds, only supports two engines [0, 1]')

	def PlayBothEngines(self) -> None:
		self.PlayEngine(engine_num=0, play=True)
		self.PlayEngine(engine_num=1, play=True)

	def DisableNonDisplayedEngine(self) -> None:
		"""Stop playing the engine not being displayed to save resources.
		"""
		current_index = self.ownerComp.par.Currentindex

		# turn off whatever engine is not being displayed
		if current_index == 0:
			self.PlayEngine(engine_num=1, play=False)
		elif current_index == 1:
			self.PlayEngine(engine_num=0, play=False)

	def GetCurrentIndex(self) -> int:
		return self.ownerComp.par.Currentindex.eval()

	def GetFadingIndicator(self) -> float:
		return self.ownerComp.par.Fadingindicator.eval()

	def TransitionToxs(self, fade_time: float = None) -> None:
		"""Transition between the two engines, fade using a switch."""
		# TODO?: Other transition options, I seperated this in case.

		if fade_time is None:
			# use default in Fadetime param
			self.ownerComp.par.Fade.pulse()
		else:
			# overwrite Fadetime param then fade 
			# (NOTE: this is the new default now)
			self.ownerComp.par.Fadetime = fade_time
			self.ownerComp.par.Fade.pulse()

	def LoadNewTox(
		self, 
		tox_path, 
		play: bool = False, 
		current_index: int = None
	) -> None:
		if current_index is not None:
			current_index = self.GetCurrentIndex()

		replace_index = None

		if current_index == 0:
			replace_index = 1
		elif current_index == 1:
			replace_index = 0

		if replace_index is not None:
			self.ownerComp.par[f'File{replace_index}'] = tox_path
			self.PlayEngine(engine_num=replace_index, play=play)

	def LoadNewToxAndTransition(
		self, 
		tox_path,
		play: bool = False, 
		fade_time: float = None
		) -> None:
		current_index = self.GetCurrentIndex()
		fading_indicator = self.GetFadingIndicator()

		if fading_indicator == 0:
			self.LoadNewTox(tox_path=tox_path, play=play)
			self.TransitionToxs(fade_time=fade_time)


	# def myFunction(self, v):
	# 	debug(v)

	# def PromotedFunction(self, v):
	# 	debug(v)