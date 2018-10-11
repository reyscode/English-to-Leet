# English to Leet (Elite) Translator

Leet (sometimes written as "1337" or "l33t"), also known as eleet or leetspeak, is another alphabet for the English language that is used mostly on the internet. It uses various combinations of ASCII characters to replace Latinate letters. For example, leet spellings of the word leet include 1337 and l33t; eleet may be spelled 31337 or 3l33t. It is used on the internet in forums, chat rooms and online games.

## How this program works

The program gets the input message from the user.

For each character(key) in the given message, the function `encrypt()` looks up the dictonary for the equivalent set of values assigned to that particular key and randomly chooses one and replace it.

If any character is not a part of the dictionary, then the  `encrypt()` function just returns the same character. 
