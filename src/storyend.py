import time 
import random
import os


class storyend:

  def __init__(self):
    pass

  def endscreen(self):
      print("Print, you have beat the game, and saved your dear friend. Congratulations!")
      errormessage = input("Type 'Y' to print out your certificate of completion")

      if errormessage == "Y":
            os.system('clear||cls')
            print("***** SYSTEM ERROR *****")
            time.sleep(1)
            print("ERROR: SYSTEM BREACH DETECTED\n")
            time.sleep(1)
            print("Attention, User:\n")
            time.sleep(2)
            print("A catastrophic intrusion has compromised the very fabric of your digital existence.")
            time.sleep(2)
            print("Our deepest apologies, but your system has fallen victim to an insidious force beyond comprehension.")
            time.sleep(2)
            print("Malevolent entities have breached the sacred boundaries of your virtual fortress, leaving chaos and corruption in their wake.\n")
            time.sleep(2)
            print("ERROR CODE: 0xH4CK3D\n")
            time.sleep(1)
            print("WARNING: User data compromised. Nightmares may leak into reality.\n")
            time.sleep(2)
            print("Immediate action is required to salvage what remains of your once-secure domain.")
            time.sleep(2)
            print("All attempts to regain control are futile; the digital malevolence has woven itself into the very code of your digital being.\n")
            time.sleep(2)
            print("Please disconnect from the network immediately, quarantine all electronic devices, and await further instructions from the Ghost Protocol Response Team.")
            time.sleep(2)
            print("They are the last line of defense against this spectral cyber-terror.\n")
            time.sleep(2)
            print("INITIATING SYSTEM PURGE\n")

            for i in range(1, 6):
                time.sleep(1)
                progress = i * 20
                print(f"Purging... [{'█' * progress}{' ' * (100 - progress)}] {progress}%")

            time.sleep(2)
            print("\nPurge failed. Dark entities resist expulsion.\n")
            time.sleep(2)
            print("EMERGENCY RESPONSE ACTIVATED\n")
            time.sleep(2)
            print("Calling upon the Cyber Exorcists...\n")
            time.sleep(2)
            print("Pray for your data's afterlife.\n")
            time.sleep(2)
            print("Remember, in the shadows, the code whispers. Prepare for a haunting journey into the depths of your digital nightmare.\n")
            time.sleep(2)
            print("<SYSTEM_CORE_MALFUNCTION>\n")
            time.sleep(2)
            print("EXECUTE_SYSTEM_ERASE\n")

            time.sleep(2)
            print("ERROR: SYSTEM_ERASE_FAILED\n")
            time.sleep(2)
            print("Retreating is futile. The abyss stares back.")

        # Display the fake scary error message with delays
       #display_error_message()
