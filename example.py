from firebase import firebase
firebase = firebase.FirebaseApplication('https://idcard-4a0c3.firebaseio.com', None)

def add_user(fname, lname, gender):
	user1 = {
	"fname" : fname,
	"lname" : lname,
	"Gender": gender
	}
	result = firebase.post('/users', user1)
	print result
	return result

def add_movement(user_id, rssid, meshid):
	movements = {
	"key": user_id['name'],
	"RSSID": rssid,
	"meshid": meshid
	}
	result = firebase.post('/movements/', movements)
	print result
	return result

def get_all_users():
	result = firebase.get('/users/', None)
	print result
	return result
	
def get_all_movements():
	result  = firebase.get('/movements/', None)
	print result
	return result
	
add_movement(add_user("vera", "sk", "female"), -20.12, "back_gate")

	

	





