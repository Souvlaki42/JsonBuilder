from timeit import default_timer as timer
import sys

def handlePossibeErrors(lambdaFunctionToExecute, printDebuggingMessage = False, detailedLog = False):
	if printDebuggingMessage: timerStarting = round(timer() * 1000)
	try:
		return lambdaFunctionToExecute()
	except Exception as e:
			print(f"Error: {e}")
			if detailedLog:
				exception_type, exception_object, exception_traceback = sys.exc_info()
				filename = exception_traceback.tb_frame.f_code.co_filename
				line_number = exception_traceback.tb_lineno

				print(f"Type: {exception_type}")
				print(f"File name: {filename}")
				print(f"Line number: {line_number}")
	finally:
		if printDebuggingMessage: timerStopping = round(timer() * 1000)
		if printDebuggingMessage: print(f"JSON executed in {timerStopping-timerStarting} ms")