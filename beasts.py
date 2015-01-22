import random
import re
import string
 
class Beast():
    def __init__(self):
        # word lists
        self.sourceDb = {} 
        
        # BEAST NAME
        self.sourceDb['prefix'] = ["Ana","Bandi","Andro","Cata","Bush","Mino","Baha","Blue","Cy","Kar","Dra","Echo","Pan","Azu","Awa","Chi","Di","Ipo","Kele","Vexa","Nea","Qua","Ven","Howl","Pon","Lich"]
        self.sourceDb['suffix'] = ["bist","tier","man","core","phon","by","py","mir","la","ris","bus","tane","phine","mean","don","thon","dian","phane","don","corn","ven","tor","fiend","bhan"] 
        
        # BEAST DESCRIPTION
        self.sourceDb['thing'] = ["creature","beast","monster","animal"]
        self.sourceDb['bodypart'] = ["body","head","tail"]
        self.sourceDb['animal'] = ["an antelope","a human","a lion","a dog","a pig","a scorpion","a flea","a bat","a snake","an axolotl"]
        
        # ATTRIBUTE 1
        self.sourceDb['ability'] = ["run","scream","jump","speak","fight","heal things","research things","do magic","fly"]
        self.sourceDb['abilityadverb'] = ["slowly","for a long time","with its mind","with great care","like the wind","very quickly","with little effort","better than humans","with less skill than most humans","if backed into a corner","only once a year","when peer-pressured","beyond the ken of humankind","in a way that makes one shudder","to the point of tears","more swiftly than an eagle","for days on end without pause","suddenly and without warning","unerringly"]
        
        # ATTRIBUTE 2
        self.sourceDb['attribute'] = ["Its *bodypart* is *bodypartdesc*"]
        self.sourceDb['bodypartdesc'] = ["*bodyadj* enough to *verb* a human","used for wooing potential mates","used to *verb* other creatures"]
        self.sourceDb['bodyadj'] = ["strong","cool","powerful","large","shocking"]
        self.sourceDb['verb'] = ["kill","overwhelm","stun","attract","intimidate"]
        
        # ATTRIBUTE 3
        self.sourceDb['voice'] = ["voice","call","mating call","roar"]
        self.sourceDb['sound'] = ["an airhorn","a set of panpipes","bones rattling","a garbage disposal","wind chimes","baby talk","a fire crackling","an electric guitar riff","an accordian song","a lion's roar","the dial-up noise","static","a penguin laughing","a door slamming","a vacuum cleaner","a crow's caw","a burbling creek","the toot of a recorder"]
        
        # ORIGIN
	self.sourceDb['originated'] = ["was first observed","first appeared in texts", "was originally depicted"]
	self.sourceDb['reason'] = ["the minion of a God","a children's story","a protecter of the weak","a trickster","an old wive's tale","a fairy tale","an ancient earth spirit","an invasive species from space","a legend","a failed experiment","the product of a magic spell","a witch's familiar","a work animal"]
        
        # NATURE 1
        self.sourceDb['adverb'] = ["often","usually","sometimes","traditionally","typically"]
        self.sourceDb['adjective'] = ['boisterous','pleasant','polite','loving','vile','angry','skittish','grumpy', 'tough','absent-minded','frustrated','annoying','bothersome','vicious','rabid','sweet','agreeable']
        
        # NATURE 2
        self.sourceDb['humaninteraction'] = ["It enjoys *verbing* humans","*doesnt*","It does not distinguish between humans and animals","It can be found wherever humans gather","Reports suggest it will try to integrate itself into any human community it finds","Sometimes one can be seen begging for food at scrap-heaps and cemeteries"]
        self.sourceDb['doesnt'] = ["It doesn't interact with humans","No human has ever seen one", "No one has seen one and lived to tell about it"]
        self.sourceDb['verbing'] = ["eating","playing with","dancing with","observing","tricking","mocking","bothering","kissing","attacking","wrestling","mentoring","manipulating","helping","visiting","avoiding","hiding from","murdering","killing","stalking","admiring","spending time with","ignoring","laughing at","dating","dressing up","cheering up","performing for"]

	# NATURE 3  
        self.sourceDb['habit'] = ["scavenging for items","exploring the wilderness","building dens","hunting for sport","lazing about","scheming","interfering with the affairs of others"]
        self.sourceDb['desire'] = ["create art","travel the world","learn the meaning of life","rule the world","raise a family","find true love","become famous","develop an interesting skill","survive in a harsh world","defeat its rivals","make new friends","run the animal kingdom","get a bad reputation"]
       
        # DIET
        self.sourceDb['food'] = ["nuts","bugs","pizza","fruit","wheat","rodents","humans","popcorn","mangos","rocks","small animals","its parents","memories","burnt offerings","thunderclouds","snakes","the eyes of birds and fish","strong spirits","carrion","small woodland villages"]
        
        # HUNTING GROUNDS
        self.sourceDb['geofeature'] = ["tidal pools","mountains","plains","tundra","forests","beaches","deserts","rocky regions","rainforests","flood zones","foothills"]
        self.sourceDb['geolocation'] = ["Asia","Africa","Europe","Antarctica","North America","South America","Australia"]

        #text output
        self.output = ""

    def replace_words(self, string):
        while "*" in string:
            m = re.search('\*(.+?)\*', string)
            if m:
                word = m.group(1)
                replacer = "*"+word+"*"
                string = string.replace(replacer, random.choice(self.sourceDb[word]),1)
        return string

    def make_image(self, string1, string2, string3):
    	str1 = string1.split(" ")
    	str2 = string2.split(" ")
    	str3 = string3.split(" ")
    	
    	string1 = str1[1]
    	string2 = str2[1]
    	string3 = str3[1]
    	
    	string = '<img src="images/' + string1 + 'tail.png" style="position: absolute;"/>'
    	string = string + '<img src="images/' + string2 + 'body.png" style="position: absolute;"/>'
    	string = string + '<img src="images/' + string3 + 'head.png" style="position: relative;"/>'
    	
    	return string

    def make_stuff(self):
        beastname = self.replace_words("*prefix**suffix*")
        
        ani1 = self.replace_words("*animal*")
        ani2 = self.replace_words("*animal*")
        ani3 = self.replace_words("*animal*")
        aniImage = self.make_image(ani1,ani2,ani3)
        
        desc1 = self.replace_words("A *thing* with the head of "+ani3+",")
        desc2 = self.replace_words(" the body of "+ani2+",")
        desc3 = self.replace_words(" and the tail of "+ani1+".")
        
        n = str(random.randint(4,19))
        orig = self.replace_words("It *originated* in the "+n+"th century as *reason*.")
        
        attr = self.replace_words("It can *ability* *abilityadverb*. *attribute*.")
        attr = attr + "<br/><br/>"
        attr = attr + self.replace_words("Its *voice* resembles *sound*.")
        
        nature = self.replace_words("The creature is *adverb* *adjective*. *humaninteraction*.")
        nature = nature + "<br/><br/>"
        nature = nature + self.replace_words("It spends its days *habit*. It yearns to *desire*.")
        
        diet = self.replace_words(beastname+"s *adverb* eat *food* and *food*.")
        
        ground = self.replace_words("Can be found in the *geofeature* of *geolocation*.")
        
        self.output = "<div>"
        self.output = self.output + aniImage
        self.output = self.output + "</div>"
        self.output = self.output + "<h2>----- "+beastname+" -----</h2>"
        self.output = self.output + desc1 + desc2 + desc3 + "<br/><br/>"
        self.output = self.output + "<h2>----- ORIGIN -----</h2>"
        self.output = self.output + orig + "<br/><br/>"
        self.output = self.output + "<h2>----- ATTRIBUTES -----</h2>"
        self.output = self.output + attr + "<br/><br/>"
        self.output = self.output + "<h2>----- NATURE -----</h2>"
        self.output = self.output + nature + "<br/><br/>"
        self.output = self.output + "<h2>----- DIET -----</h2>"
        self.output = self.output + diet + diet2 + "<br/><br/>"
        self.output = self.output + "<h2>----- HUNTING GROUNDS -----</h2>"
        self.output = self.output + ground + "<br/><br/>"

    def make(self):
        # make the output
        self.make_stuff()

        # put it on the site
        print self.output

beast = Beast()
beast.make()