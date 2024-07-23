from pynput import keyboard
import pyperclip
import pyautogui
import re

def get_vowel(string):
    match = re.search("[aeiouwAEIOUW].*",string)
    if match:
        return match.group(0)
    else:
        return None

def get_consonant(string):
    match = re.search("^(.*?)[aeiouwAEIOUW]", string)
    if match:
        return match.group(1)
    else:
        return None

def swap_numerals(string):
    new_string = ""
    for c in string:
        new_string += numerals_replacements[c]
    pyperclip.copy(new_string)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('space')


# Define the dictionary of replacements
vowels_replacements = {
    "eeb":"𖬀𖬶","eem": "𖬀","eej":"𖬀𖬰","eev":"𖬀𖬲","ee":"𖬁","ees":"𖬁𖬰","eeg":"𖬁𖬲",
    "ib":"𖬂𖬲","im":"𖬂","ij":"𖬂𖬰","iv":"𖬂𖬶","i":"𖬃","is":"𖬃𖬰","ig":"𖬃𖬲",
    "aub":"𖬄𖬰","aum":"𖬄","auj":"𖬄𖬶","auv":"𖬄𖬲","au":"𖬅","aus":"𖬅𖬰","aug":"𖬅𖬲",
    "ub":"𖬆𖬰","um":"𖬆","uj":"𖬆𖬶","uv":"𖬆𖬲","u":"𖬇","us":"𖬇𖬰","ug":"𖬇𖬲",
    "eb":"𖬈𖬰","em":"𖬈","ej":"𖬈𖬲","ev":"𖬉","e":"𖬉𖬰","es":"𖬉𖬲","eg":"𖬉𖬶",
    "aib":"𖬊𖬰","aim":"𖬊","aij":"𖬊𖬶","aiv":"𖬊𖬲","ai":"𖬋","ais":"𖬋𖬰","aig":"𖬋𖬲",
    "oob":"𖬌","oom":"𖬌𖬰","ooj":"𖬌𖬲","oov":"𖬍","oo":"𖬍𖬰","oos":"𖬍𖬲","oog":"𖬍𖬶",
    "awb":"𖬎","awm":"𖬎𖬰","awj":"𖬎𖬲","awv":"𖬎𖬶","aw":"𖬏","aws":"𖬏𖬰","awg":"𖬏𖬲",
    "uab":"𖬐𖬶","uam":"𖬐","uaj":"𖬐𖬰","uav":"𖬐𖬲","ua":"𖬑","uas":"𖬑𖬲","uag":"𖬑𖬶",
    "ob":"𖬒𖬰","om":"𖬒","oj":"𖬒𖬲","ov":"𖬒𖬶","o":"𖬓𖬰","os":"𖬓𖬲","og":"𖬓",
    "iab":"𖬔","iam":"𖬔𖬰","iaj":"𖬔𖬶","iav":"𖬔𖬲","ia":"𖬕","ias":"𖬕𖬰","iag":"𖬕𖬲",
    "ab":"𖬖𖬲","am":"𖬖","aj":"𖬖𖬰","av":"𖬗","a":"𖬗𖬰","as":"𖬗𖬲","ag":"𖬗𖬶",
    "wb":"𖬘𖬰","wm":"𖬘","wj":"𖬘𖬲","wv":"𖬙","w":"𖬙𖬰","ws":"𖬙𖬲","wg":"𖬙𖬶"
}

consonants_replacements = {
    "v":"𖬜","nr":"𖬜𖬰","f":"𖬜𖬵","nts":"𖬝","ts":"𖬝𖬰","ph":"𖬝𖬵",
    "hn":"𖬩","kh":"𖬩𖬰","nt":"𖬩𖬵","n":"𖬬","nq":"𖬬𖬰","nqh":"𖬬𖬵",
    "y":"𖬤","nc":"𖬤𖬰","s":"𖬤𖬵","x":"𖬮","":"𖬮𖬰","ny":"𖬮𖬵",
    "qh":"𖬣","hny":"𖬣𖬰","hm":"𖬣𖬵","l":"𖬞","d":"𖬞𖬰","dh":"𖬞𖬵",
    "plh":"𖬪","tsh":"𖬪𖬰","p":"𖬪𖬵","ch":"𖬧","xy":"𖬧𖬰","t":"𖬧𖬵",
    "h":"𖬟","th":"𖬟𖬰","pl":"𖬟𖬵","c":"𖬯","ntsh":"𖬯𖬰","tx":"𖬯𖬵",
    "nth":"𖬫","npl":"𖬫𖬰","nkh":"𖬫𖬵","nch":"𖬨","nrh":"𖬨𖬰","np":"𖬨𖬵",
    "ml":"𖬠","hml":"𖬠𖬰","ng":"𖬠𖬵","r":"𖬡","nph":"𖬡𖬰","nplh":"𖬡𖬵",
    "m":"𖬦","txh":"𖬦𖬰","q":"𖬦𖬵","nk":"𖬢","ntx":"𖬢𖬰","rh":"𖬢𖬵",
    "hl":"𖬥","z":"𖬥𖬰","ntxh":"𖬥𖬵","k":""
}

numerals_replacements = {
    "0":"𖭐","1":"𖭑","2":"𖭒","3":"𖭓","4":"𖭔","5":"𖭕","6":"𖭖","7":"𖭗","8":"𖭘","9":"𖭙"
}

# Initialize a buffer to store typed characters
buffer = ""

def on_press(key):
    global buffer
    try:
        # Add the character to the buffer
        buffer += key.char
        print(f"Buffer: {buffer}")
    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.space:
            vowel = get_vowel(buffer)
            consonant = get_consonant(buffer)
            if vowel in vowels_replacements and consonant in consonants_replacements:
                # Replace the buffer content with the corresponding text
                pyautogui.hotkey('shift', 'ctrl','left')
                word = vowels_replacements[vowel] + consonants_replacements[consonant]
                pyperclip.copy(word)
                pyautogui.hotkey('ctrl','v')
                pyautogui.press('space')  # Add a space to complete the input
                buffer = ""
            # Replace arabic numerals with pahawh numerals
            if re.search("[0-9]*",buffer).group(0) != "":
                pyautogui.hotkey('shift', 'ctrl','left')
                swap_numerals(buffer)
                buffer = ""
            else:
                buffer = ""
        if key == keyboard.Key.backspace:
            buffer = buffer[:-1]

def on_release(key):
    # Stop listener
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
