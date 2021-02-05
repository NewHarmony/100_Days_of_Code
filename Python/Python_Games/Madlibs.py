story_num = int(input("Welcome to Madlibs! Please pick a story by entering a number from 0-3. "))

adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
verb1 = input("Verb: ")
verb2 =  input("Verb: ")
famous_person1 = input("Famous person: ")
famous_person2 = input("Famous person: ")

madlib1 = f"Twinkle Twinkle {adj2} {famous_person1}, how I wonder what you are. Up above the world so {adj1}, like a diamond in the sky. \
When the blazing {famous_person2} is gone, When he nothing {verb2} upon, Then you {verb1} your little light, Twinkle, twinkle, all the night."

madlib2 = f"“The {adj1} {famous_person1} {verb1} up the water spout.Down came the rain, and {verb2} the {famous_person1} out. \
Out came the sun, and dried up all the rain, and the {adj2} {famous_person1} went up the water spout"

madlib3 = f"{famous_person1} had a {adj2} lamb, whose fleece was {adj1} as snow. And everywhere that {famous_person1} went, \
the lamb was sure to go. It followed {famous_person1} to school one day which was against the rules. \
It made {famous_person2} {verb1} and {verb2}, to see a lamb at school."

madlib4 = f"O {famous_person1}, O {famous_person1}, How {adj1} are thy branches! Not only {adj2} when summer’s here \
But in the coldest time of year. O {famous_person1}, O {famous_person1}, How {adj1} are thy branches!"

madlib_list = [madlib1,madlib2,madlib3,madlib4]

madlib = madlib_list[story_num]

print(madlib)

