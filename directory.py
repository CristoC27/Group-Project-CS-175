# Dictionaries contain room numbers and names associated with that room
basement_main = {"GHA10" : "", "AUD" : "", "W2" : "Office of Admission Processing", "W3" : "", "W4" : "Purchasing Accounts Payable", "W5": "", "W6" : "Withey Chapel"}
first_main = {"104" : "Julian Francis Abele Room", "106" : "Cafe", "107" : "", "108" : "Financial Aid", "109" : "Office of Admissions","110" : "Bursar's Office/Cashier's Office"}
second_main = {"201" : "Office of Graduate Admission", "203" : "Office of Conference Services and Special Events/Central Scheduling", "205" : "Institutional Review Board/Institutional Animal Care and Use Committee/Institutional Research & Effectiveness","206" : "Middle States Commission on Higher Education", "207" : "", "208" : "Office of the Registrar","209" : "", "210" : "Associate Provost", "211" : "Provost/Senior VP for Academic Affairs/Director of Academic Finance","213" : "Office of the President","217" : "VP and Chief Business Officer/Associate VP for Finance and Budget","218" : ""}
third_main = {"301" : "Administrative Offices" , "302" : "Administrative Offices", "303" : "Administrative Offices", "304" : "Vice President and General Counsel", "305" : "Office of Equity & Diversity and Internal Audit", "306": "", "307" : "","308" : "VP for Enrollment Management","309" : "", "310" : "", "311" : "","312" : "Office of Human Resources","313" : "","314" : "", "315" : "","316" : "","317" : "VP for University Advancement","319": "", "320": "","321" : "Stewardship and Donor Relations","322" : "Office of Student Employment"}

basement_office = {"W11" : "Prof. Aristy-Reyes, Coppola, Hamlet, Kachinsky, O’Connell, Rubin, and Varga","W12" : "Prof. Fabian, Bates, Tepedino, and Van Clef","W13" : "Prof. Gold","W14" : "","W15" : "Prof. Zaldotti","W16" : "Under Construction","W17" : "Under Construction"}
first_office = {"W22" : "Department of English"}
half_office = {"400" : "","401" : "","402" : "Prof. Vurro","403" : "Prof. Graedon","404" : "Dr. Fury","405" : "Prof. Cook and Prof. Belinski","406" : "Dr. Goulding","407" : "Prof. Jacomme and Dr. Sood","408" : "Prof. Swanson and Prof. Bogert","409" : "Dr. Vetere","410" : "Prof. Vercher","411" : "Dr. Womack, MFA Program Director"}
second_office = {"501" : "Dr. Gilmartin, Department Advising Coordinator and Prof. Pachucki","502" : "Dr. Blair", "503" : "Prof. Torchia and Prof. Marousis-Bush","504" : "Dr. Siracusa and Dr. Biesiada","505" : "Dr. Werner Director of First Year Composition","506" : "Prof. Sacks and Prof. Wedlock", "507" : "Dr. Love, Associate Director of First Year Composition","508" : "Dr. Starke, Undergraduate Program Coordinator","509" : "Dr. Bluemel","510" : "","511" : "Copy Room"}

dicts = [basement_main, first_main, second_main, third_main, basement_office, first_office, half_office, second_office]
# Breaks up directions into "building blocks" to allow for easier time creating directions for rooms
start = "From the main entrance,"
main_stairs = "the main stairs,"
stairs = "the stairs to the"
small_stair = "the second set of stairs and"
left_turn = "turn left,"
right_turn = "turn right,"
up = "go up"
down = "go down"
straight = "walk forward and"
first = "first room on the"
second = "second room on the"
third = "third room on the"
fourth = "fourth room on the"
fifth = "fifth room on the"
sixth = "sixth room on the"
seventh = "seventh room on the"
eighth = "eighth room on the"
destination = "your destination is the"

bath_floors = ["B","2"]
room = ""
# Takes input and formats it to be usable by program and returns it to get_room() function
async def room_format():
	global room
	room = await input("Enter room in the Great Hall that you want directions to : ")
	room = str(room)
	room = room.upper()
	if "GH" in room:
		room = room.replace("GH", "")
	if "ROOM" in room:
		room = room.replace("ROOM", "")
	room = room.replace(" ", "")
	return room
# Changes input further to match dictionary keys and returns room number
async def get_room():
	global room
	await room_format()
	if "BATH" in room or "REST" in room:
		room = "BATHROOM"
		return room
	elif "AUD" in room:
		room = "AUD"
		return room
	elif "A10" in room:
		room = "GHA10"
		return room
	elif "W" in room:
		return room
	while len(room) != 3 and room.isdigit():
		print("Room not found, please enter new room,")
		await room_format()

# Prints directions to main rooms on basement level
def direct_b1(r):
	if basement_main[r] == "":
		print(f"Directions to room {r} {basement_main[r]}:\n")
	else:
		print(f"Directions to room {r} \n{basement_main[r]}:\n")
	if r == "GHA10":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} basement and {straight} {left_turn} {straight} {destination} room in front of you")
	elif r == "AUD":
		print(f"{start} {down} {main_stairs} {destination} room in front of you")
	elif r == "W2":
		print(f"{start} {down} {main_stairs} {left_turn} {straight} {destination} {first} right")
	elif r == "W3":
		print(f"{start} {down} {main_stairs} {left_turn} {straight} {destination} {third} right")
	elif r == "W4":
		print(f"{start} {down} {main_stairs} {left_turn} {straight} {destination} {fourth} left")
	elif r == "W5":
		print(f"{start} {down} {main_stairs} {left_turn} {straight} {destination} {third} left")
	elif r == "W6":
		print(f"{start} {down} {main_stairs} {left_turn} {straight} {destination} {second} left")
# Prints directions to main rooms on first level
def direct_f1(r):
	if first_main[r] == "":
		print(f"Directions to room {r} {first_main[r]}:\n")
	else:
		print(f"Directions to room {r} \n{first_main[r]}:\n")
	if r == "104":
		print(f"{start} go past {main_stairs} {right_turn} {straight} {destination} {first} left")
	if r == "106":
		print(f"{start} {right_turn} {destination} room in front of you")
	if r == "107":
		print(f"{start} go past {main_stairs} {left_turn} {straight} {left_turn} {destination} room in front of you")
	if r == "108":
		print(f"{start} go past {main_stairs} {left_turn} {straight} {left_turn} {destination} {first} right")
	if r == "109":
		print(f"{start} go past {main_stairs} {left_turn} {destination} room in front of you")
	if r == "110":
		print(f"{start} go past the cafe, {right_turn} {straight} {right_turn} {straight} {destination} {second} left")
# Prints directions to main rooms on second level
def direct_f2(r):
	if second_main[r] == "":
		print(f"Directions to room {r} {second_main[r]}:\n")
	else:
		print(f"Directions to room {r} \n{second_main[r]}:\n")
	if r == "201":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} {destination} {second} left")
	if r == "203":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} {straight} turn right at the end of the hallway, {straight} turn left at the end of the hallway, {straight} turn left at the end of the hallway, {destination} room on the right")
	if r == "205":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} {straight} turn right at the end of the hallway, {destination} room in front of you")
	if r == "206":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} {straight} turn right at the end of the hallway, {straight} turn right at the end of the hallway, {straight} {destination} {first} left")
	if r == "207":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} {straight} turn right at the end of the hallway, {straight} turn right at the end of the hallway, {straight} turn left at the recess, {destination} room on the left")
	if r == "208":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} turn left at the end of the hallway, {straight} turn left at the end of the hallway, {straight} turn right at the recess, {destination} room in the middle")
	if r == "209":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} turn left at the end of the hallway, {straight} turn left at the end of the hallway, {straight} turn right at the recess, {destination} room on the right")
	if r == "210":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} turn left at the end of the hallway, {straight} turn left at the end of the hallway, {straight} {destination} door on the right")
	if r == "211":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} turn left at the end of the hallway, {destination} door at the end of the hallway")
	if r == "213":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} turn left at the end of the hallway, {straight} {destination} {first} right ")
	if r == "217":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {destination} {second} right")
	if r == "218":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {destination} {first} right")
# Prints directions to main rooms on third level
def direct_f3(r):
	if third_main[r] == "":
		print(f"Directions to room {r} {third_main[r]}:\n")
	else:
		print(f"Directions to room {r} \n{third_main[r]}:\n")
	if r == "301" or r == "302" or r == "303":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {destination} room on the left")
	if r == "304":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {left_turn} {destination} room in front of you")
	if r == "305":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {left_turn} {destination} room on the right")
	if r == "306":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} turn left at the end of the hallway, {straight} {destination} room on the left")
	if r == "307":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} turn left at the end of the hallway, {destination} room in front of you")
	if r == "308":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {destination} room at the end of the hallway")
	if r == "309":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} at the end of the hallway {right_turn} {destination} {first} left")
	if r == "310":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} at the end of the hallway {right_turn} {destination} {second} left")
	if r == "311":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {right_turn} {straight} turn left at the end of the hallway, {straight} turn left at the end of the hallway, {destination} {first} right")
	if r == "312":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {right_turn} {straight} turn left at the end of the hallway, {straight} {destination} room at the end of the hallway")
	if r == "313":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {right_turn} {straight} turn left at the end of the hallway, {straight} {destination} room on the right at the end of the hallway")
	if r == "314":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {right_turn} {straight} turn left at the end of the hallway, {straight} at the recess {right_turn} {destination} {first} left")
	if r == "315":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {right_turn} {straight} turn left at the end of the hallway, {straight} at the recess {right_turn} {destination} {second} left")
	if r == "316":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {right_turn} {straight} turn left at the end of the hallway, {straight} at the recess {right_turn} {destination} {first} right")
	if r == "317":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {right_turn} {straight} turn left at the end of the hallway, {straight} at the recess {right_turn} {destination} {second} right")
	if r == "319":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {right_turn} {straight} {destination} {fourth} right")
	if r == "320":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {right_turn} {straight} {destination} {third} right")
	if r == "321":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {right_turn} {straight} {destination} {second} right")
	if r == "322":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {right_turn} {straight} {destination} {first} right")
# Prints directions to office rooms on second floor
def direct_o2(r):
	if second_office[r] == "":
		print(f"Directions to room {r} {second_office[r]}:\n")
	else:
		print(f"Directions to room {r} \n{second_office[r]}:\n")
	if r == "501":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {seventh} left ")
	if r == "502":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {eighth} right ")
	if r == "503":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {seventh} right ")
	if r == "504":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {fourth} right ")
	if r == "505":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {third} right ")
	if r == "506":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {first} right ")
	if r == "507":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {first} left ")
	if r == "508":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {third} left ")
	if r == "509":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {fourth} left ")
	if r == "510":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {fifth} left ")
	if r == "511":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {sixth} left ")
# Prints directions to office rooms on 1.5th floor
def direct_o15(r):
	if half_office[r] == "":
		print(f"Directions to room {r} {half_office[r]}:\n")
	else:
		print(f"Directions to room {r} \n{half_office[r]}:\n")
	if r == "400":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} next level and {destination} room in front of you")
	if r == "401":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} next level and {left_turn} {straight} {destination} {third} left")
	if r == "402":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} next level and {left_turn} {straight} {destination} {third} right")
	if r == "403":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} next level and {left_turn} {straight} {destination} {second} right")
	if r == "404":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} next level and {right_turn} {straight} {destination} {first} left")
	if r == "405":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} next level and {right_turn} {straight} {destination} {second} left")
	if r == "406":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} next level and {right_turn} {straight} {destination} {fourth} left")
	if r == "407":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} next level and {right_turn} {straight} {destination} {fourth} right")
	if r == "408":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} next level and {right_turn} {straight} {destination} {second} right")
	if r == "409":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} next level and {right_turn} {straight} {destination} {first} right")
	if r == "410":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} next level and {left_turn} {straight} {destination} {first} left")
	if r == "411":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} next level and {left_turn} {straight} {destination} {second} left")
# Prints directions to office room on first floor
def direct_o1(r):
	print(f"Directions to room {r} \n{first_office[r]}:\n")
	print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} first floor and {destination} room on the left")
# Prints directions to office rooms on basement level
def direct_ob(r):
	if basement_office[r] == "":
		print(f"Directions to room {r} {basement_office[r]}:\n")
	else:
		print(f"Directions to room {r} \n{basement_office[r]}:\n")
	if r == "W11":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} basement and {destination} room on the left")
	if r == "W12":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} basement and {straight} {destination} room on the right")
	if r == "W13":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} basement and {right_turn} {straight} {right_turn} {straight} {left_turn} {straight} {destination} {first} right")
	if r == "W14":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} basement and {right_turn} {straight} {right_turn} {straight} {left_turn} {straight} {destination} {second} right")
	if r == "W15":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} basement and {right_turn} {straight} {right_turn} {straight} {left_turn} {straight} {destination} {third} right")
	if r == "W16" or r == "W17":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} basement and {straight} {left_turn} {straight} {destination} room on the right")
	# Prints directions to bathrooms
def direct_bath(f):
	if f == "B":
		print("\nDirections to Men's Bathroom in basement:\n")
		print(f"{start} {down} {main_stairs} {left_turn} {straight} at first room on left {left_turn} {straight} {right_turn} {straight} {destination} room on the left")
		print("\nDirections to Women's Bathroom in Basement:\n")
		print(f"{start} {down} {main_stairs} {right_turn} {straight} {destination} room in front of you")
		print("\nDirections to Gender Neutral Bathroom in Basement:\n")
		print(f"{start} {down} {main_stairs} {right_turn} {straight} {destination} room on the left at the end of the hallway")
		print("\nDirections to Gender Neutral Bathroom in Basement (Office Side):\n")
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {down} {stairs} basement and {destination} room in front of you")

	if f == "2":
		print("\nDirections to Women's Bathroom on Second Floor:\n")
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} {straight} turn right at the end of the hallway, {straight} turn left at the end of the hallway, {straight} turn left at the end of the hallway, {straight} turn right at the end of the hallway, {destination} room in front of you")
		print("\nDirections to Men's Bathroom on Second Floor:\n")
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} {straight} turn right at the end of the hallway, {straight} turn left at the end of the hallway, {straight} turn right at the end of the hallway, {straight} {left_turn} {destination} room in front of you")
		print("\nDirections to Women's Bathroom on Second Floor (Office Side):\n")
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {fifth} right ")
		print("\nDirections to Gender Neutral Bathroom on Second Floor (Office Side):\n")
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} go through the door and {right_turn} to the end of the hallway {straight} {left_turn} {straight} {destination} {sixth} right ")


while True:
	print("")
	found = False
	while not found:
		await get_room()
	# Will find bathroom on given level when print directions
		if room == "BATHROOM":
			found = True
			print("1B: B\n2F: 2")
			bath_floor = await input("what floor do you want to find a bathroom on?: ")
			bath_floor = str(bath_floor)
			bath_floor = bath_floor.upper()
			while bath_floor not in bath_floors:
				print("There is no bathroom on that floor, please enter a valid floor")
				print("1B: B\n2F: 2")
				bath_floor = await input("what floor do you want to find a bathroom on?: ")
				bath_floor = str(bath_floor)
				bath_floor = bath_floor.upper()
			print("FOUND")
			direct_bath(bath_floor)
		else:
	# Determines if room is in dictionaries and therefore in building
			for floor in dicts:
				if room in floor:
					found = True
					print("FOUND!")
			if not found:
				print("Room not found, please enter new room")
	print("")
	# Calls a direction function based on what dictionary the room is found in
	if room in basement_main:
		direct_b1(room)
	if room in first_main:
		direct_f1(room)
	if room in second_main:
		direct_f2(room)
	if room in third_main:
		direct_f3(room)
	if room in second_office:
		direct_o2(room)
	if room in half_office:
		direct_o15(room)
	if room in first_office:
		direct_o1(room)
	if room in basement_office:
		direct_ob(room)
