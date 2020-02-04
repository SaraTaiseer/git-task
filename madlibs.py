def main():
        print ("Mad libs where libs get mad.")
        print ("Start below:")
        time = int(input("Enter a number from 1 to 12:"))
        items= input("Enter a noun (plural):")
        name = input("Enter a name:")
        scream = input("Enter any sentence")
        action=input("Enter a verb")

        print ("\n The story goes...")
        print ("\n It was %d o'clock when I heard a knock at the door."%(time))
        print ("I opened the door and there was abox full of "+items+" with a note saying \"From Mr. "
        +name.capitalize()+".\"")
        print ("Just as I closed the door I heard a scream \" "+scream.upper()+".\"")
        print ("I froze in place and all I could do was"+action)
                     
	# write your code here



if __name__ == '__main__':
	main()
