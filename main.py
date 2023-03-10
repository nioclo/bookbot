with open("books/frankenstein.txt") as file:
    file_contents = file.read()

    chars = {}
    for l in range(ord("a"), ord("z") + 1):
        chars.update({chr(l): 0})

    for c in file_contents:
        if "a" <= c.lower() <= "z":
            chars[c.lower()] += 1
    
    print(f"--- Begin report of {file.name} ---")
    print(f"{len(file_contents.split())} words found in the document\n")
    for i in sorted(chars.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")