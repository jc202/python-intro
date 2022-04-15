#Author: Justin Chisholm

action = input("What would you like to do? (V)iew signs, or see your (F)ortune: ").lower()

if action == "v":
    print(f"""
          Astrological Signs Dates
          -Aries: March 21 - April 19
          -Taurus: April 20 - May 20
          -Gemini: May 21 - JUne 21
          -Cancer: June 22 - July 22
          -Leo: July 23 - August 22
          -Virgo: August 23 - September 22
          -Libra: September 23 - October 23
          -Scorpius: October 24 - November 21
          -Sagittatius: November 22 - December 21
          -Aquarius: January 20 - February 18
          -Pisces: February 19 - March 20
          """)
elif action == "f":
    zodiac = input("Enter your sign: ").lower()
    if zodiac == "aries":
        print("Lower your guard and others will do the same.")
    elif zodiac == "taurus":
        print("You will take a step out of your comfort zone, and it will pay off.")
    elif zodiac == "gemini":
        print("Invest in a great jacket and a better financial advisor. You'll need it.")
    elif zodiac == "cancer":
        print("It's finally your time. Audition to put on the Cocky suit!")
    elif zodiac == "leo":
        print("Someone you know has big news.")
    elif zodiac == "virgo":
        print("A friend will approach you with a new business venture.")
    elif zodiac == "libra":
        print("Winter will bring you new opportunities.")
    elif zodiac == "scorpio":
        print("Be cautious. The next few days may be peculiar.")
    elif zodiac == "saggitarius":
        print("The winds of change are blowing your way. Make sure to prepare for it.")
    elif zodiac == "capricorn":
        print("You'll receive a unexpected call today. Be sure to answer it..")
    elif zodiac == "aquarius":
        print("Today's your lucky day! Scratch off some numbers!")
    elif zodiac == "pisces":
        print("You'll find an old face when you visit a new place.")
print("Have a nice day!")