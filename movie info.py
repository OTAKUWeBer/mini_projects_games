class movie:
    def __init__(self, name, release, link, duration):
        self.name = name
        self.release = release
        self.link = link
        self.duration = duration
        
    def print_details(self):
        print("Movie Name:", self.name)
        print("Release:", self.release)
        print("Link:", self.link)
        print("Duration:", self.duration)
        print()

three_idiots = movie('3 idiots', '25 December , 2009' , 'IMBD 8.4⭐: https://www.imdb.com/title/tt1187043/', '2 hours 50 min')
krrish_3 = movie('Krrish 3' , '1 November , 2013' , 'IMBD 5.3⭐: https://www.imdb.com/title/tt1029231/' , '2 hours 51 min')
enthiran = movie('Enthiran' , '1 October , 2010' , 'IMBD 7.1⭐: https://www.imdb.com/title/tt1305797/' , '2 hours 54 min')

print ('We got 3 movies information for now.\n1. 3 idiots\n2. Krrish 3\n3. Enthiran ')
while True:
    choose = input('Enter the movie Name or number to check a few details (enter "exit" to quit):\n')
    if choose.lower() == '3 idiots' or choose == '1' :
        three_idiots.print_details()
    elif choose.lower() == 'krrish 3' or choose == '2' :
        krrish_3.print_details()
    elif choose.lower() == 'enthiran' or choose == '3' :
        enthiran.print_details()
    elif choose.lower() == "exit":
        break
    else:
        print('We got 3 movies information for now.\n1. 3 idiots\n2. Krrish 3\n3. Enthiran\n')