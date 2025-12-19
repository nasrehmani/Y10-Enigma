def single_rotor_encrypt(letter, rotor_position):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # 1. Define the internal wiring of a real Enigma rotor (Rotor I)
    # This means: Input 'A' becomes 'E', 'B' becomes 'K', etc.
    rotor_wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    
    # 2. Convert the input letter to a number (0-25)
    # ord('A') is 65. So ord(letter) - 65 gives us 0 for A, 1 for B...
    input_index = ord(letter.upper()) - 65
    
    if input_index < 0 or input_index > 25:
        return letter # Return special chars (spaces, punctuation) as is
    
    # 3. Apply the Shift (The Rotation)
    # If the rotor is at position 'B' (1), everything shifts by 1.
    # We use modulo (%) 26 so it wraps around (Z -> A).
    shifted_index = (input_index + rotor_position) % 26
    
    # 4. Pass through the wiring
    # Find which letter comes out of the wire at that index
    output_letter_from_wiring = rotor_wiring[shifted_index]
    
    # 5. Convert that output letter BACK to an index to handle the output shift
    # In a real machine, the output contact also rotates.
    output_wiring_index = ord(output_letter_from_wiring) - 65
    final_index = (output_wiring_index - rotor_position) % 26
    
    # 6. Convert number back to letter
    final_letter = alphabet[final_index]
    
    return final_letter

# --- TEST THE CODE ---
while (True):
  
  message = input("Enter your message")
  if message.lower() == "end":
        print("Exiting program. Auf Wiedersehen!")
        break
  position = 1 # Imagine the rotor is turned to position 'B'
  encrypted_message = ""
  for char in message:
    encrypted_message += single_rotor_encrypt(char, position)

  print(f"Original: {message}")
  print(f"Encrypted (Rotor Pos {position}): {encrypted_message}")
