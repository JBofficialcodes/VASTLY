import random

fun_destinations = [ "Atlanta Black Museum" , "Break Room" ,  "Escape Room" ,  "WhiteWaters SixFlags" ,  "Selfie Museum" , "Ponce City Market and Rooftop" , "Illuminarium" ,  "Cake and Sip" , "Skyline Park" ,  "Sugar Factory", "Epix Movie Theater" ,  "Candle Lit Atlanta" , "PunchBowl" , "PuttShack" , "The Bando" ]

destination = input( "What type activity are you looking for? (Dining, Thrills, Family Fun, Sports, Outdoors, Kid Activities, Adult Activities): ")


if destination == "Dining":
	print( "Good food is the way to a good mood! Here's some top recommendations! Magianno's Little Itlay, No Mas! Cantina, PitBoss Atlanta, Red Orchid Thai Cuisine, Golden Corral, Chili's, and American Deli" )
	response = input("Random Acitvities (Yes/No)?: ")
	while response == "Yes":
		print( "Here's some random activities!: " , end = '' )
		print(random.choice(fun_destinations))
		response = input("Other Random Acitvities (Yes/No)?: " )


if destination == "Thrills":
	print( "Here's some recommendations for those who love the thrill! Six Flags, Andretti Karting & Games, Bowlero, Paintballing, Cascade, and Skyzone " )
	response = input("Random Acitvities (Yes/No)?: ")
	while response == "Yes":
		print( "Here's some random activities!: " , end = '' )
		print(random.choice(fun_destinations))
		response = input("Other Random Acitvities (Yes/No)?: " )

if destination == "Family Fun":
	print( "Have the best exprience with your family with these recommendations! Georgia Aquarium, World of Coke, Botanical Gardens, Zoo Atlanta, Civil Right Museum, )." )
	response = input("Random Acitvities (Yes/No)?: ")
	while response == "Yes":
		print( "Here's some random activities!: " , end = '' )
		print(random.choice(fun_destinations))
		response = input("Other Random Acitvities (Yes/No)?: " )

if destination == "Sports":
	print( "Atlanta Falcons Football, Atlanta United Soccer, Atlanta Hawks Basketball, Atlanta Braves Baseball, Atlanta Dream WNBA, University Sports  " )
	response = input("Random Acitvities (Yes/No)?: ")
	while response == "Yes":
		print( "Here's some random activities!: " , end = '' )
		print(random.choice(fun_destinations))
		response = input("Other Random Acitvities (Yes/No)?: " )

if destination == "Outdoors":
	print( "Here's some recommendations for the great outdoors! Piedmont Park, Stone Mountain Parks, Lake Lanier, Botanical Gradens, Centennial Olympic Park, and Mural and Public Art." )
	response = input("Random Acitvities (Yes/No)?: ")
	while response == "Yes":
		print( "Here's some random activities!: " , end = '' )
		print(random.choice(fun_destinations))
		response = input("Other Random Acitvities (Yes/No)?: " )

if destination == "Kid Activities":
	print( " Let the kids run  wild with these acvities! Childrens Museum of Atlanta, Center for Puppetry Arts, Main Event, Fernbank Museum, Fernbank Science Museum, LegoLand Atlnata ." )
	response = input("Random Acitvities (Yes/No)?: ")
	while response == "Yes":
		print( "Here's some random activities!: " , end = '' )
		print(random.choice(fun_destinations))
		response = input("Other Random Acitvities (Yes/No)?: " )

if destination == "Adult Activities":
	print( "Fat Tuesday, The Battery, Atlantic Station, Magic City, ATL Sip & Paint, Luna Lounge )." )
	response = input("Random Activities (Yes/No)?: ")
	while response == "Yes":
		print( "Here's some random activities!: " , end = '' )
		print(random.choice(fun_destinations))
		response = input(" Other Random Activities (Yes/No)?: " )


print("Yayy, now go have fun! Your adventure awaits! ")
