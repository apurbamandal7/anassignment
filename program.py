def function1(start_time, answer_time, resolved_time, abandoned_time):
	#predicted_time is the time to predict the time an issue needs to be assigned to an agent
	predicted_time = start_time - answer_time + resolved_time + abandoned_time
	
function1(10, 11, 30, 12)