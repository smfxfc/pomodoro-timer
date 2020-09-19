#! python3

class TimerError(Exception):
	"""A custom exception used to report errors in use of the Timer class."""

class Timer:
	def __init__(self):
		self.__start_time = None

	def start(self):
		"""Start a new timer."""
		if self.__start_time is not None:
			raise TimerError(f"Timer is running. Use .stop() to stop the timer.")

		self.__start_time = time.perf_counter()

	def stop(self):
		"""Stop the timer, and report the elapsed time."""
		if self.__start_time is None:
			raise TimerError(f"Timer is not running, so it can't be stopped. Use .start to start the timer.")

		elapsed_time = time.perf_counter() - self.__start_time

		self.__start_time = None
