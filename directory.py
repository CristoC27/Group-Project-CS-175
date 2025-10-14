floor_1_landmarks = ["Main Stairs"]
floor_2_landmarks = ["Piano","Bust","Table with Flowers"]
floor_3_landmarks = ["Emergency Police Phone","HR Bulletin Board","Student Employment Door"]

basement_main = {"GHA10" : "", "AUD" : "", "W2" : "Office of Admission Processing", "W3" : "", "W4" : "Purchasing Accounts Payable", "W5": "", "W6" : "Withey Chapel"}
first_main = {"104" : "Julian Francis Abele Room", "106" : "Cafe", "107" : "", "108" : "Financial Aid", "109" : "Office of Admissions","110" : "Bursar's Office/Cashier's Office"}
second_main = {"201" : "Office of Graduate Admission", "203" : "Office of Conference Services and Special Events/Central Scheduling", "205" : "Institutional Review Board/Institutional Animal Care and Use Committee/Institutional Research & Effectiveness","206" : "Middle States Commission on Higher Education", "207" : "", "208" : "Office of the Registrar","209" : "", "210" : "Associate Provost", "211" : "Provost/Senior VP for Academic Affairs/Director of Academic Finance","213" : "Office of the President","217" : "VP and Chief Business Officer/Associate VP for Finance and Budget","218" : ""}
third_main = {"301" : "Administrative Offices" , "302" : "Administrative Offices", "303" : "Administrative Offices", "304" : "Vice President and General Counsel", "305" : "Office of Equity & Diversity and Internal Audit", "306": "", "307" : "","308" : "VP for Enrollment Management","309" : "", "310" : "", "311" : "","312" : "Office of Human Resources","313" : "","314" : "", "315" : "","316" : "","317" : "VP for University Advancement","319": "", "320": "","321" : "Stewardship and Donor Relations","322" : "Office of Student Employment"}

basement_office = {"W011" : "Prof. Aristy-Reyes, Coppola, Hamlet, Kachinsky, O’Connell, Rubin, and Varga","W012" : "Prof. Fabian, Bates, Tepedino, and Van Clef","W013" : "Prof. Gold","W014" : "","W015" : "Prof. Zaldotti","W016" : "Under Construction","W017" : "Under Construction"}
first_office = {"W22" : "Department of English"}
half_office = {"400" : "","401" : "","402" : "Prof. Vurro","403" : "Prof. Graedon","404" : "Dr. Fury","405" : "Prof. Cook and Prof. Belinski","406" : "Dr. Goulding","407" : "Prof. Jacomme and Dr. Sood","408" : "Prof. Swanson and Prof. Bogert","409" : "Dr. Vetere","410" : "Prof. Vercher","411" : "Dr. Womack, MFA Program Director"}
second_office = {"501" : "Dr. Gilmartin, Department Advising Coordinator and Prof. Pachucki","502" : "Dr. Blair", "503" : "Prof. Torchia and Prof. Marousis-Bush","504" : "Dr. Siracusa and Dr. Biesiada","505" : "Dr. Werner Director of First Year Composition","506" : "Prof. Sacks and Prof. Wedlock", "507" : "Dr. Love, Associate Director of First Year Composition","508" : "Dr. Starke, Undergraduate Program Coordinator","509" : "Dr. Bluemel","510" : "","511" : "Copy Room"}

dicts = [basement_main, first_main, second_main, third_main, basement_office, first_office, half_office, second_office]

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
destination = "your destination is the"

bath_floors = ["B","1","2","3"]
room = ""
room_list = ""

def room_format():
	global room
	room = input("Enter room in the Great Hall that you want directions to : ").upper()
	if "GH" in room:
		room = room.replace("GH", "")
	if "ROOM" in room:
		room = room.replace("ROOM", "")
	room = room.replace(" ", "")
	return room
def get_room():
	global room
	global room_list
	room_format()
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
		room_format()
	if room.isdigit():
		room_list = room[:1] + "," + room[1:]
		room_list = room_list.split(",")
		room_list = list(map(int,room_list))
		return room, room_list
def direct_b1(r):
	print(f"Directions to room {r} {basement_main[r]}:")
	if r == "GHA10":
		print(f"{start} {up} {main_stairs} {left_turn} {up} {small_stair} {right_turn} {straight} to the end of the "
			  f"hallway and {right_turn} {straight} {left_turn} {straight} {down} {stairs} basement, {straight} {left_turn} {destination} room in front of you ")
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
def direct_f1(r):
	print(f"Directions to room {r} {first_main[r]}:")
	if r == "104":
		print(f"{start} go past {main_stairs} {right_turn} {straight} {destination} {first} right")
	if r == "106":
		print(f"{start} {right_turn} {destination} room in front of you")
	if r == "107":
		print(f"{start} go past {main_stairs} {left_turn} {straight} {left_turn} {destination} room in front of you")
	if r == "108":
		print(f"{start} go past {main_stairs} {left_turn} {straight} {left_turn} {destination} {first} right")
	if r == "109":
		print(f"{start} go past {main_stairs} {left_turn} {destination} room in front of you")
	if r == "110":
		print(f"{start} go past the cafe, {right_turn} {straight} {right_turn} {destination} {first} left")
def direct_f2(r):
	print(f"Directions to room {r} {second_main[r]}:")
	if r == "201":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} {destination} {second} left")
	if r == "203":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} {straight} turn right at the end of the hallway, {straight} turn left at the end of the hallway, {straight} {left_turn} {destination} on the right")
	if r == "205":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} {straight} turn right at the end of the hallway, {straight} turn right at the end of the hallway, {destination} {first} left")
	if r == "206":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} {straight} turn right at the end of the hallway, {straight} turn right at the end of the hallway, {destination} {second} left")
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
def direct_f3(r):
	print(f"Directions to room {r} {third_main[r]}:")
	if r == "301" or r == "302" or r == "303":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {destination} room on the left")
	if r == "304":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {left_turn} {destination} room in front of you")
	if r == "305":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} {left_turn} {destination} room on the right")
	if r == "306":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} to the end of the hallway, {left_turn} {straight} {destination} room on the left")
	if r == "307":
		print(f"{start} {up} {main_stairs} {right_turn} {up} {small_stair} {left_turn} go through the first door on the left, {up} {stairs} third floor and go through the door and {right_turn} {straight} to the end of the hallway, {left_turn} {destination} room in front of you")
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

found = False
while not found:
	get_room()
	if room == "BATHROOM":
		found = True
		print("1B: B\n1F: 1\n2F: 2\n3F: 3")
		bath_floor = input("what floor do you want to find a bathroom on?: ").upper()
		while bath_floor not in bath_floors:
			print("Bathroom not found, please enter a valid floor")
			print("1B: B\n1F: 1\n2F: 2\n3F: 3")
			bath_floor = input("what floor do you want to find a bathroom on?: ").upper()
		print("FOUND")
	elif "AUD" in room or "W" in room or "GHA10" in room:
		for floor in dicts:
			if room in floor:
				found = True
				print("FOUND!")
				true_floor = floor
		if not found:
			print("Room not found, please enter new room")
	else:
		for floor in dicts:
			if room in floor:
				found = True
				print("FOUND!")
		if not found:
			print("Room not found, please enter new room")
print("")
if room in basement_main:
	direct_b1(room)
if room in first_main:
	direct_f1(room)
if room in second_main:
	direct_f2(room)
if room in third_main:
	direct_f3(room)
