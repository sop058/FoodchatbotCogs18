"""A collection of function for doing my project."""

#ends the chat when the user type 'quit'
def end_chat(input_list):
    if 'quit' in input_list:
        return True
    return False


#suggests Korean food when the user type 'k' for msg variable
def korean_food(vegan, protein):
    #list of Korean food
    korean_menu = ['Tofu Soup', 'Budae Jjigae', 'Kimch Fried Rice','Steamed Chicken',
                       'Naengmyeon','Galbitang','Japchae','Bulgogi']
    spicy = input('Do you like spicy food? y or n ')
    
    #checks for end_chat
    if end_chat(spicy):
        return 'Bye!'
    soup = input('Do you like soupy food? y or n ')
    if end_chat(soup):
        return 'Bye!'
    
    print('\n')
    spicy.lower()
    soup.lower()

    #when the user wants spicy food
    if spicy == 'y':
        #if the user wants soupy and vegan food
        if soup == 'y' and vegan == "y":
            print('I suggest ' + korean_menu[0] + '.')
        #if the user wants soupy food
        elif soup == 'y' and vegan == 'n':
            print('I suggest ' + korean_menu[1] + '.')
            print('I suggest ' + korean_menu[0] + ' with ' + protein + '.')
        #if the user wants non soupy and vegan food
        elif soup == 'n' and vegan == 'y':
            print('I suggest ' + korean_menu[2] + '.')
        #if the user wants non soupy food
        elif soup == 'n' and vegan == 'n':
            print('I suggest ' + korean_menu[3] + '.')
            print('I suggest ' + korean_menu[2] + ' with ' + protein + '.')
    #when the user wants non spicy food
    else:
        if soup == 'y' and vegan == "y":
            print('I suggest ' + korean_menu[4] + '.')
        if soup == 'y' and vegan == 'n':
            print('I suggest ' + korean_menu[5] + '.')
        if soup == 'n' and vegan == "y":
            print('I suggest ' + korean_menu[6] + '.')
        if soup == 'n' and vegan == 'n':
            print('I suggest ' + korean_menu[7] + '.')
    
    return None


#suggests Chinese food when the user type 'c' for msg variable
def chinese_food(vegan, protein):
    #list of Chinese food
    chinese_menu = ['Hot Pot','Noodle Soup','Hot Sour Soup',
                        'Dim Sum','Jjajangmyeon','Mapo Tofu','Roasted Duck']
    
    soup = input('Do you like soupy food? y or n ')
    #checks for end_chat
    if end_chat(soup):
        return 'Bye!'

    print('\n')
    soup.lower()

    #when the user wants soupy food
    if soup == 'y':
        if vegan == 'y': 
            print('I suggest ' + chinese_menu[0] + '.')
            print('I suggest ' + chinese_menu[1] + '.')
        else:
            print('I suggest ' + chinese_menu[0] + ' with ' + protein + '.')
            print('I suggest ' + chinese_menu[1] + ' with ' + protein + '.')
            print('I suggest ' + chinese_menu[2] + '.')
    #when the user wants non soupy food
    else:
        if vegan == 'y':
            print('I suggest ' + chinese_menu[4] + '.')
            print('I suggest ' + chinese_menu[5] + '.')

        else:
            print('I suggest ' + chinese_menu[3] + ' with ' + protein + '.')
            print('I suggest ' + chinese_menu[4] + ' with ' + protein + '.')
            print('I suggest ' + chinese_menu[6] + '.')
            
    return None


#suggests Japanese food when the user type 'j' for msg variable
def japanese_food(vegan, protein):
    #list of Japanese food
    japanese_menu = ['Udon','Soba','Ramen','Yakisoba','Sushi',
                         'Chirashi Bowl','Curry','Kama','Tonkatsu']
    noodle = input("Do you like noodle? y or n ")
    #checks for end_chat
    if end_chat(noodle):
        return 'Bye!'
    noodle.lower()
    
    #when the user wants noodle
    if noodle == 'y':
        if vegan == 'y':
            print('\n')
            print('I suggest ' + japanese_menu[0] + '.')
            print('I suggest ' + japanese_menu[1] + '.')
            print('I suggest ' + japanese_menu[2] + '.')
            print('I suggest ' + japanese_menu[3] + '.')
        else:
            print('\n')
            print('I suggest ' + japanese_menu[0] + ' with ' + protein + '.')
            print('I suggest ' + japanese_menu[2] + ' with ' + protein + '.')
            print('I suggest ' + japanese_menu[3] + ' with ' + protein + '.')
    #when the user doesn't want noodle
    else:
        if vegan == 'n':
            print('I suggest ' + japanese_menu[6] + ' with ' + protein + '.')
        else:
            raw = input("Do you like raw fish? y or n ")
            print('\n')
            if end_chat(raw):
                return 'Bye!'
            raw.lower()
            if raw =='y':
                print('I suggest ' + japanese_menu[4] + '.')
                print('I suggest ' + japanese_menu[5] + '.')
            else:
                print('I suggest ' + japanese_menu[6] + ' with ' + protein + '.')
                print('I suggest ' + japanese_menu[7] + '.')
                print('I suggest ' + japanese_menu[8] + '.')
    return None



#asks questions to the user and apply the previous functions
def meal():
    out_msg = None
    chat = True
    protein = None
    while chat:
        msg = input('Welcome to East Asia. Which cuisine would you like:' 
                    '(K)orean, (C)hinese, (J)apanese? ')
        #checks for end_chat
        if end_chat(msg):
            out_msg = 'Bye!'
            break
        vegan = input('Are you a vegan? y or n ')
        if end_chat(vegan):
            out_msg = 'Bye!'
            break
        if vegan == 'n':
            protein = input('What do you want as your protein? ')
            if end_chat(protein):
                out_msg = 'Bye!'
                break

        msg.lower()
        vegan.lower()
        
        #use korean_food function
        if msg == 'k': 
            out_msg = korean_food(vegan, protein)
        
        #use chinese_food function        
        if msg == 'c':
            out_msg = chinese_food(vegan, protein)
        
        #use japanese_food function            
        if msg == 'j':
            out_msg = japanese_food(vegan, protein)
            
        if out_msg != None:
            break
            
        print('\n')
    
    print(out_msg)