# data_structures.py

from Resources.classes import Job

BN = [
    "James", "John", "Michael", "David", "Daniel", "Matthew", "Ethan", "Joshua", 
    "Alexander", "Ryan", "William", "Samuel", "Benjamin", "Lucas", "Jacob", "Isaac", 
    "Nathan", "Oliver", "Max", "Jack", "Adam", "Tyler", "Henry", "Carter", "Luke", 
    "Dylan", "Owen", "Caleb", "Noah", "Joseph", "Andrew", "Luke", "Zachary", "Isaiah", 
    "Christian", "Logan", "Austin", "Tyson", "Cole", "Thomas", "Jacob", "Eli", "Bennett", 
    "Xander", "Grayson", "Calvin", "Victor", "Evan", "George", "Jackson", "Tristan", 
    "Aiden", "Wyatt", "Jordan", "Miles", "Bob", "Joe", "Fred"
]

# -------------------------------------------------------

GN = [
    "Mary", "Elizabeth", "Sarah", "Jessica", "Emily", "Emma", "Sophia", "Olivia", 
    "Ava", "Isabella", "Grace", "Charlotte", "Lily", "Mia", "Amelia", "Abigail", "Hannah", 
    "Chloe", "Madison", "Harper", "Ella", "Lily", "Aubrey", "Scarlett", "Zoe", "Layla", 
    "Evelyn", "Victoria", "Sophie", "Maya", "Riley", "Leah", "Ariana", "Hailey", "Madeline", 
    "Savannah", "Addison", "Gabriella", "Audrey", "Quinn", "Kylie", "Lila", "Cora", "Stella", 
    "Penelope", "Kaitlyn", "Aria", "Brianna", "Kayla", "Megan", "Camila", "Sadie", 
    "Isla", "Rosa", "Odeldl", "Fredina"
]

# -------------------------------------------------------

LN = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", 
    "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", 
    "Thompson", "Garcia", "Martinez", "Roberts", "Clark", "Rodriguez", "Lewis", 
    "Walker", "Young", "Allen", "King", "Scott", "Green", "Adams", "Baker", "Nelson", 
    "Hill", "Carter", "Mitchell", "Perez", "Robinson", "Phillips", "Evans", "Turner", 
    "Collins", "Edwards", "Stewart", "Morris", "Murphy", "Cook", "Rogers", "Gutierrez", 
    "Diaz", "Kim", "Bell", "Wood", "Howard", "Richards", "Bennett", "Mason"
]

# -------------------------------------------------------

sponsors = {}
sponsors["NordVPN"] = "Want to feel protected on the internet? Well, sorry to burst your bubble but you arent! The only solution is to get NordVPN! NordVPN doesent give you protection either, but it makes you feel like you are protected. So give us your money! Go to NordVPN.com/temubitlife for a 50% on for 4 months!"
sponsors["Pie Adblocker"] = "Want to never watch an ad like this? Download Pie Adblocker! We are not sketchy and will never collect your data and sell it to consumers. Download now at pie.org/temubitlife"
sponsors["Honey"] = "Do you want to save MONEY? Well fear not! Download Honey and get free discount codes that work! We are 100% not stealing affileater codes and taking all of the profits to outselves! Join Honey!"
sponsors["Temu"] = "Do you hate shopping, trying to find a good deal? Well with Temu, you can get 'high quality' items for 'very cheap'! We are 100% not in any FBI investigation. Trust us! Go to temu.com/temubitlife for -10% off your next order!"
sponsors["Raid Shadow Legends"] = "Raid Shadow Legends is a turn based rpg done right. In case you've been living under a rock and haven't heard, raid is a badass mobile game that changes everything. The game is crazy popular, with almost 15 million downloads in the last 6 months. Raid is an epic dark fantasy done right. A hero collecting turn based game with over 400 champions to collect and customize. In raid you can get knights orcs undead and more. Raid with friends in a clan, claim glory in the pvp arena. Some other cool features are multi battle auto mode, set battles to run in auto mode while you do something else. Spend less time grinding and more time developing your team and finding the fun stuff. They also have weekly tournaments and events, such as fighting in the arena, running special dungeons, or leveling up your hero's. There's always a way to compete and win extra prizes every week. The game is growing super fast, check out this road map they've published. They actually have huge plans for updates over the next 6 months. There's Infinite content for you to enjoy no time to get bored. A new faction, a tag team arena feature, and even a new clan boss you'll be able to fight with your clan mates.Go to raidshadowlegends.com/temubitlife for a FREE 50% off with NO money back guarantee! Start your journey today!"
sponsors["World of Tanks"] = "Ever wanted to be a tank mechanic? Ever wanted to drive a tank around like a boss? Well, download World of Tanks! Drive around historical vehicles like the Tiger I, the Sherman tank, and many more! Use code TEMUBITLIFE for a 0% off and a FREE random tank (100% not rigged.)"
sponsors["World Thunder"] = "Ever wanted to fly a airplane? Ever wanted to operate a submarine? Ever wanted to fight in the trenches? All without risk? Well download War Thunder, a free, reliable, multiplayer roleplay game! We offer thousands of vehicles and game modes that can entertain you for hours. Download War Thunder and use code TEMUBITLIFE in the shop for 5000 tokens. (Expect tokens in 1 - 400 business years.)"
sponsors["Beijing Corn"] = "Nice corn, it tasts so good. You think it is made in the United States, because they are the largest producer of corn. You read the label on the back 'Made in China' you think WHAT DA HAIL??? You realize that you arent eating normal corn, you are eating BEIJING CORN. Beijing Corn is the best corn brand, created by Steven He, your truly. 'Tastes like failure' says Steven He. Go to beijingcorn.com/temubitlife to get one FREE shipment of Beijing Corn containing one (1) container. NOTE: Beijing Corn might be poisonous. No promises."

# -------------------------------------------------------

doctor = Job("Doctor", 110000, "Bob Hospitals, Inc", "Junior Doctor", [("Junior Doctor", 110000) ,("Doctor", 120000), ("Senior Doctor", 140000), ("Head Doctor", 170000)])
lawyer = Job("Lawyer", 90000, "Bob, Joe & Fred", "Junior Attorney", [("Junior Attorney", 90000), ("Attorney", 110000), ("Senior Attorney", 130000), ("Head Attorney", 160000)])
engineer = Job("Engineer", 80000, "Bob Construction, Inc", "Junior Engineer", [("Junior Engineer", 80000), ("Engineer", 90000), ("Head Engineer", 120000), ("Head Engineer", 150000)])
teacher = Job("Teacher", 63000, "Bob Elementaty School", "Kindergarten Teacher", [("Kindergarten Teacher", 63000), ("First Grade Teacher", 68000), ("Second Grade Teacher", 73000), ("Third Grade Teacher", 78000), ("Fourth Grade Teacher", 83000), ("Fifth Grade Teacher", 88000), ("Vice Princical", 98000), ("Principal", 5)])
jobless = Job("Jobless", 10000, "Nobody", "NA", [("Jobless", 10000)])
storeworker = Job("Storeworker", 28000, "Bob Grocery", "Junior Cashier", [("Junior Cashier", 28000), ("Cahier", 38000), ("Senior Cashier", 45000), ("Head Cashier", 50000)])
joblessK = Job("Jobless", 0, "NA", "NA", [("NA", 0)])
basicjobs = [doctor, lawyer, engineer, teacher, storeworker]
