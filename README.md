TimeCalcShell
=============

Calculate time :)


Usage
=====

with debug enabled (input string, operations, result, history, result):
	+0.023s #>__10:00 + 3:00 + 14:33 - 20:00__
	OP ADD  10.0
	OP ADD   3.0
	OP ADD 14.55
	OP SUB  20.0
	-------
	7.55
	['+', '10:00', '+', '3:00', '+', '14:33', '-', '20:00']
	7.55

without debug:	
	+0.013s #>14:33
	14.55