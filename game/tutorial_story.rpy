$ renpy.include("inventory.rpy")

# Declare characters used by this game.
define r = Character(_("Receptionist"), color="#c8ffc8")
define t = Character(_("Toni"), color ="#ffffff")
define p = Character(_("Me"), color="#c8c8ff")
define c = Character(_("Cathy"), color="#dde100")

image Receptionist="receptionist.png"
image Toni="tony.png"
image Toni smile="tony_smile.png"
image Toni wave="tony_wave.png"
image Me="playermale.png"
image cathy="Cathy.png"

image secret doc="secret_doc.jpg"
image bd phone="bg phone.png"
image bg reception="reception.png"
image bg reception2="reception2.png"
image bg office="bg office.jpeg"
image bg laptop="bg laptop.png"
image bg laptop2="bg laptop2.png"
image bg coffee = "bg coffee.png"
image bg desktop ="bg top_secret_desktop.png"

label tutorial:

    call inventory

    # scene bg entryhall 

    scene bg reception
    show Me with easeinright
    show Receptionist with easeinleft
    
    r "Good morning. Are you new here? What’s your name?"

    define p = Character("[povname]", color="#c8c8ff")

    python:
        style.input.color = "#ffffff"
        povname = renpy.input("Type in your name:", length=15)
        povname = povname.strip()


    p "Yes, it’s my first day here."

    r "Nice to meet you [povname]! I will call Toni to tell him that you are here. He will do the onboarding process with you."

    scene bg office

    show Toni with easeinleft
    show Me with easeinright

    t "Hey there, welcome to the team!"
    t "I am Toni. Today, on your first day at work, I'm going to help you get settled into the company and get to grips with everything."

    #menu: 

    p "Thank you. Nice to meet you!"
    hide Toni
    show Toni smile
    t "If you not already aware: Tasty Food Co. is a global leader in agriculture and nutrition. We utilize the power and provisions of nature to generate safe, healthy, and sustainable nutrition for people around the world."

    t "Your new job role is pretty awesome. You're our go-to person for keeping our computer systems super secure. Think of it as being a detective for our computers. You're on the lookout for any weak spots that could be trouble."
    
    t "We're thrilled to have you on board, making sure our company's network is strong and ready for anything. Ready to dive into it? Let's do this!" 

    t "To help you understand what your job involves, here's a little exercise for you. Write a phishing email to our colleague Frank from the department."

    p "Sounds good, can you give me more information about Frank?"

    t "Frank is married, has two children and a cat named Lucy. In his free time, he enjoys cycling and hiking. He is also good friends with his colleague Jane Thompson. That’s all I personally know."

    p "Great. Thanks!"

    t "On the right upper corner, you can find your notebook. When you click it, you will find your goal for the level, the information you will gather throughout your work and the people you will meet along the way. You can try it out!" #Highlight Notebook Icon

    define toni = Person("Toni", "images/tony.png", "Colleague")

    $ people.add_person(toni)

    define frank_info = InventoryData("Information about Frank", "married, two children, owns a cat named Lucy, enjoys cycling and hiking, good friends with colleague Jane Thompson")

    $ inventory.add_data(frank_info)

    $ todo.update_aim("Write a phishing email")

    "{i}Toni, your new goal, and the information about Frank were added to your notebook.{\i}"

    scene bg office
    show Toni wave
    show Me 

    t "Here is your work laptop. Everything is already set up for you. I now have to leave you for today. I will be in an important conference for the rest of the day. See you tomorrow!"

    p "All right then I'll get started. See you!"
    hide Toni wave with easeoutleft

    t "Mhh.. I wonder what kind of phishing email would Frank fall for..."
    #scene laptop email
    hide screen inv_screen
    jump phishing

label phishing:

    scene black
    call screen phishing

screen phishing:
    add "images/bg laptop2.png"
    imagebutton auto "gui/phishing_mails/mail1_%s.png":
        focus_mask True
        action Jump("right_phishing")

    imagebutton auto "gui/phishing_mails/mail2_%s.png":
        focus_mask True
        action Jump("wrong_phishing")


label wrong_phishing:
    t "Mhh I don't think this is the right choice. If I remember correctly Frank is more into cats."
    jump phishing

label right_phishing: 
    show bg desktop
    t "Haha, that Frank guy is not a very smart one! Now I have access to his computer screen."
    t "Oh what's in that folder?"

label password_story:

    show screen inv_screen
    show bg laptop
    scene laptop top secret
    show bg laptop2
    t "It's password protected."
    t "If I remember correctly, then the most common passwords are 123456, password, and qwerty. I could just try them out"

    label password:
        python:
            style.input.color = "#ffffff"
            password = renpy.input("", length=32, screen = "nameInput")
            password = password.strip()

    if password == "qwerty":
        jump right
        
    else:
        "Wrong Password! I should try an alternative..."
        jump password


label right:

    "That worked! Ok what is this?"

    #Show PDF Top Secret Document
    show secret doc at Position(ypos=0.8) with zoomin
    pause(2.0)

    menu:

        "Download file and save on the USB drive, that you always have with you.":
            jump usb

        "Print out file and take the paper with you.":
            jump printing

        "Close the application and try forgetting about it, it's not your business.":
            jump closed


label printing:
    t "Thank God, no one saw me printing that file. Next time, I should be more careful."
    jump evidence

label usb:
    t "Now, I should get out of here quickly. I have a bad feeling about this."
    jump evidence

label closed:
    t "I don't know if this was a smart idea, but I don't feel good about it."
    jump no_evidence

label evidence:

    #transition Black
    scene black
    scene bg reception2
    show Me at Position(xpos=0) 
    
    
    "5 PM closing time… Your first day at work is finished. You leave the place hasty, to get to the appointment with your friend Cathy in time."

    t "I'm just glad I'm meeting Cathy tonight and hopefully with her help, I can make a plan of what to do. I think I might be in trouble …"
    hide Me with easeoutleft
    scene bg coffee
    show Me with easeinright
    "As you are walking towards the bar, you can not get this information out of your head. Is there something illegal going on at your new working place?"
  

    show cathy with easeinleft

    c "Hey! I hope you had a nice first day at work. You look a bit stressed. Did everything go well?"

    p "No not at all. I mean at first it went well. Toni was showing me around, but then I discovered some alarming document. Some parts were even blacked out. I chose to make a copy of it. What should I do?"

    c "Ok, slow down, I think you did the right thing there."

    c "Maybe you're on to something big. Can I have a look at your evidence? I might be able to write a story about it. What do you think?"

    p "Surely this will not be easy?"

    c "Hmm, I might need more information. I will contact you on that matter! Do you have my new number already? If not maybe you should write it in your notebook"

    define cathy = Person("Cathy", "images/Cathy.png", "Reporter")

    $ people.add_person(cathy)

    define cathy_phone = InventoryData("Cathy's Phone Number", "017612345678")

    $ inventory.add_data(cathy_phone)

    "{i}Cathy and Cathy's phone number were added to your notebook.{\i}"

    p "Thank you, I got it! But now let’s not talk about work anymore."

    c "Yes, you’re right. Let’s have some drinks!"

    jump next_day

    #Transition/Finish scene in Coffee shop

label no_evidence:

    #transition Black
    scene bg reception2
    show Me at Position(xpos=0.0)
    
    

    "5 PM closing time… Your first day at work is finished. You leave the place hasty, to get to the appointment with your friend Cathy in time."

    t "I'm just glad I'm meeting Cathy tonight and hopefully with her help I can make a plan of what to do. I think I might be in trouble …"
    hide Me with easeoutleft
    scene bg coffee
    show Me with easeinright
    "As you are walking towards the bar, you can not get this information out of your head. Is there something illegal going on at your new working place?"

    show cathy with easeinleft

    c "Hey! I hope you had a nice first day at work. You look a bit stressed. Did everything go well?"

    p "No not at all I mean at first it went well. Toni was showing me around, but then I discovered some alarming document. Some parts were even blacked out. And then I tried forgetting about it because I don't want to get in trouble. But I can't get it out of my head. What should I do?"

    c " Ok slow down, without any evidence... are you trying to make a fool out of me?"

    p "No, really not, I swear on our friendship"

    #menu

    c "Can you remember anything? What was mentioned?"

    p "I remember reading about forest clearance and farmer strikes"
        
    p "I think there was the mentioning of avocados"

    p "I read the word classified"

    p "I remember something about having a surprise birthday party for the head of the department"

    # solution to not use label

    c "Maybe you're on to something big. Can I have a look at your notes? I might be able to write a story about it. What do you think?"

    p "Surely this will not be easy?"

    c "Hm, I might need more information. I will contact you on that matter! Do you have my new number already? If not maybe you should write it in your notebook"
    

    define cathy = Person("Cathy", "images/Cathy.png", "Reporter")

    $ people.add_person(cathy)

    define cathy_phone = InventoryData("Cathy's Phone Number", "017612345678")

    $ inventory.add_data(cathy_phone)

    "{i}Cathy and Cathy's phone number were added to your notebook.{\i}"

    p "Thank you, I got it! But now let’s not talk about work anymore."

    c "Yes, you’re right. Let’s have some drinks!"

    #Transition/Finish scene in Coffee shop

    jump next_day

label next_day:

    scene bg phone

    "Cathy: Hey, I found out by using your given information that the company CORE Commercial Construction might be involved as well. Do you think you could get information from them? I marked the building on this map. I wish you luck and keep me updated!"

    $ todo.update_aim("Get information about CORE")

    "{i}Your goal was updated. {\i}"

    #Notebook Map is introduced