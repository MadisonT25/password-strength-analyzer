# Password Strength Analyzer

## Pseudocode

START

Ask user to enter a password

Set score = 0  
Set feedback list = empty

Check if password length >= 8  
    If yes → score +1  
    If no → add "Use at least 8 characters" to feedback

Check if password has uppercase letters  
    If yes → score +1  
    If no → add "Add uppercase letter" to feedback

Check if password has lowercase letters  
    If yes → score +1  
    If no → add "Add lowercase letter" to feedback

Check if password has numbers  
    If yes → score +1  
    If no → add "Add a number" to feedback

Check if password has special characters  
    If yes → score +1  
    If no → add "Add a special character" to feedback

If score = 5 → Strength = Strong  
If score >= 3 → Strength = Moderate  
Else → Strength = Weak

Display strength and feedback

END