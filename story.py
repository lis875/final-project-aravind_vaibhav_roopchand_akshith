from config import *

detective1 = "Choose a name for a detective"
detective2 = "Choose a name for second detective"
color_prompt = "Color color which color do you want?"
movie_promt = "Enter your favourite movie"
accept_mission = "Do you want to accept this mission? \n 1. Yes \n 2. No"

jump="Do you wanna land the plane at your \n 1)desired location or do you wanna \n 2)skydive?"


para1 = f"""\n
        The story begins in the jail located in the extreme southern and
        shadiest part of the city residing the most vicious criminals across
        the world and also the notorious detective detective1 aka detective
        'bald eagle'(comes from him being eagle eyed and bald) in cell {JAIL_CELL}
        waiting to see the light since {NUMBER_OF_DAYS_IN_JAIL} days in a dimly lit cell with
        harsh flickering user_color light casting the silhouette of the man
        every other second, deafening sounds of jail mates hurling utensils
        and yelling doesn't bother him.\n
        It’s 5:30pm and the Prison guard walks by like everyday.
        The detective's eyes follow the guard's every move, a mixture
        of weariness and vigilance etched across his face. This was routine,
        predictable – or so he thought. Suddenly, a chill ran down Harper's
        spine as the guard deviated from his usual path. Something was amiss.
        In a surreal and unforeseen moment, the guard's gloved hand extended
        through the bars, dropping a user_color phone onto the cold, dirty floor.
        'Hey! You dropped your…..' the detective1 began only to realize midway
        that it's his own phone. The screen was casting an unnatural glow, in
        an otherwise dimly lit cell, reading “the only way out is accepting the
        mission'. Though skeptical and hesitant detective1 was left with no choice.
        A hesitant frown creased the detective1’s brow as he was holding his phone.
        """

hangman_hint = f"""
The key is summation of where you are and how long it’s been \n ({JAIL_CELL} + {NUMBER_OF_DAYS_IN_JAIL})
"""
hangman_input_prompt = "Enter the pin to unlock the cell"

para2 = """
        “Cell unlocks”
        “Surprising the detective the cell unlocks and lights are off. 
        The detective stood at the threshold of liberation, caught between the realms of 
        skepticism and the inexplicable. Suddenly, the phone buzzes, catching the detective's attention. 
        This time reading “You’ve got 5 mins before the security cameras and the lights turn back on. 
        Meet me in the user_color Mercedes at the north gate”.Harnessing his unparalleled intellect, 
        the detective orchestrates his escape, forging a path to his freedom.  
        """

para3 = """
        The detective approached the sleek user_color Mercedes, its windows tinted shadows that 
        concealed the orchestrator of this enigmatic rendezvous. Cautiously, the detective opens the
        door looking behind the wheel. The truth unfurled like a shocking revelation.
        The figure behind the wheel was none other than the prison guard who had initiated this mystifying sequence of events.
        The user_color Mercedes glided through the streets, weaving through the city's pulse until 
        it reached a desolate place devoid of any signs of life but a cabin. The detective is striving 
        to dissect the situation.Who is this man? Where is he headed?  What's the mission about?
        The guard unmasks himself revealing his name (detective2) his face as he explains in a hushed but deep 
        tone that he occupied the same position as the detective before he was imprisoned. The shadows of the past, 
        once confined to the recesses of his own memories, now materialized in the form of a counterpart who had 
        tread a parallel path. A profound empathy now replaced the previous curiosity.
        """

para4 = """
detective2 : Mr. Bald eagle It's time you need to know why we are here.
detective1 : Tell me 
detective2 : We got a mission, a dangerous one. Two actually. We can either hijack a plane or rob a bank and make a deal with the president. 
detective1 : What's the endgame here? 
detective2 (hesitant and lowering his gaze): It's to get your best friend detective glen released. He has been abducted by the government in one 
of their clandestine machinations. They plan to use him against you once your sentence is over.
detective1 (tears up while maintaining a small smile) : He is not just a friend he is family and I’ll do anything for the family.
detective2 (breaks the character) : You mean like Dom toretto(vin diesel) from Fast & Furious Mr. Bald eagle?
detective1 : Don't call me that again. Anyways, what did they do to him?
detective2 : I don't have all the answers but I'm sure it's something dark. Anyways, I have to leave now. I'll meet you at the same place tomorrow at 5AM. 
The phone shows you all the details. Make your decision by tomorrow  before you meet me.
detective2 drives away. Detective resides in the cabin for the night contemplating his past with his best friend.


Choose the mission 1(Plane Hijack) or 2(Bank Robbery): 
"""



para5 = """
It's 5AM, and the same car arrives. The detective boards the user_color car. 
As they get to the airport the detective2 offers detective1 a set of 3 user_color 
guns to choose from to carry out the mission.
"""

para6 = """
The bustling airport, with its familiar symphony of hurried footsteps and distant announcements, 
felt strangely alien to Detective Bald Eagle. As he approached the looming security check, 
an unspoken unease settled over him—a disquiet that seemed to emanate from the depths of years 
spent in confinement, away from the rhythms of ordinary life. 

Detective Handed over their boarding passes to the vigilant security officer and left the bag 
on the conveyor belt. The officer's nod signaled their clearance, yet the detective's unease 
lingered like a persistent shadow. Suddenly the alarm went off alerting the police who in no time 
surrounded the detective. It is at this moment that the detective's life flashed before his own eyes. 
One of the policemen slams the bald eagle's head from behind, knocking him out cold 
while yelling “He is armed with an AK47”. 
"""

para7 = """
The confident cadence of Detective Bald eagle’s steps echoed through the airport as he approached 
the security check with a gust of assuredness. Harper led as he seamlessly navigated the routine check, 
his passage was unhindered. 
Beyond the security checkpoint, the expansive airport terminal became a stage for Harper's calculated 
performance. The familiar surroundings fueled his self-assured stride, turning the airport into 
a canvas for his return. Having successfully boarded the  user_color plane, Harper's confidence 
reached its zenith. Making it more fun the cast of \nuser_movie that is movie_cast\n are on board as well. As the aircraft 
soared through the skies, the detective, with a calculated swagger, made his way to the cockpit. 
Wielding an invisible rocket launcher, he pointed it at the pilot, ready to unravel the final chapter 
of the enigma that had brought him back into the fold.
"""

para80="""
Too bad, you just failed the test. You need to set your priorities right and concentrate on the current mission.

(current mission continues)
The phone buzzes and now shows the president's phone number prompting the detective to call him.
President: Hello, who is this?
Detective(serious): You know damn well who I am.
President: Actually, I don't, I'm sorry dont waste my time.
*president hangs up*
Pilot at the point blank cracks up making the detective feel condescending. Angry detective Fires the rocket launcher exploding the whole plane.

MISSION FAILED - Detective died
"""
para81 = """
I like the dedication. Keep it up champ!

(current mission continues)
The phone buzzes and now shows the president's phone number prompting the detective to call him.
President: Hello, who is this?
Detective(serious): You know damn well who I am.
President: Actually, I don't, I'm sorry dont waste my time.
*president hangs up*
Pilot at the point blank cracks up making the detective feel condescending. Angry detective Fires the rocket launcher exploding the whole plane.

MISSION FAILED - Detective died
"""

para9= """
The confident cadence of Detective Bald eagle’s steps echoed through the airport as 
he approached the security check with a gust of assuredness. Harper led as he 
seamlessly navigated the routine check, his passage was unhindered. 

Beyond the security checkpoint, the expansive airport terminal became 
a stage for Harper's calculated performance. The familiar surroundings 
fueled his self-assured stride, turning the airport into a canvas for 
his return. Having successfully boarded the user_color plane, Harper's 
confidence reached its zenith. Making it more fun the cast of \nuser_movie that is movie_cast
are on board as well. As the aircraft soared through the skies, 
the detective, with a calculated swagger, made his way to the cockpit. 
Wielding a user_color desert eagle gun, he pointed it at the pilot, ready 
to unravel the final chapter of the enigma that had brought him back into the fold.
"""
para10="""
The phone buzzes and now shows the president's phone number prompting the detective to video call him.

President: Hello, who is this?

Detective(serious): You know damn well who I am.

President: The notorious Bald Eagle. It’s been so long since….(cuts)

Detective(While showing the gun pointed at the pilot): Stop! Let me come straight to the point. You release my friend publicly right now or I will blow up this entire plane.

President: Okay! Okay! Relax, I will release him now. Leave them alone. 

*President releases a statement that they will release the detective as he was not guilty and they made a wrongful arrest*

MISSION SUCCESSFUL

"""

para11="""
Detective is all set to skydive, heads to the emergency exit and raises his arm 
and pauses realizing he doesn't have a parachute.   

Detective forces the pilot to navigate the plane to his desired location. 
Lands in an abandoned airport, plans an escape to lead a happy life away from all the crime and his dark past.
"""

para12="""
Detective forces the pilot to navigate the plane to desired location. 
Lands in an abandoned airport, plans an escape to lead a happy life away from all the crime and his dark past.
"""