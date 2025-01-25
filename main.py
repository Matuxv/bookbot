def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        text = file_contents
        character_dict = {}

        for caracter in text.lower():
            if caracter in character_dict:
                character_dict[caracter] += 1
            else:
                character_dict[caracter] = 1

        keys_to_delete = [i for i in character_dict if not i.isalpha()]
        for key in keys_to_delete:
            del character_dict[key]

        character_list = [{"character": k, "count": v} for k, v in character_dict.items()]
        sorted_character_list = sorted(character_list, key=lambda x: x["count"], reverse=True)
            
        

        print("--- Begin report of books/frankenstein.txt ---")
        print(str(len(words)) + " words found in the document")
        print("")
        for item in sorted_character_list:
            print(f"The '{item['character']}' character was found {item['count']} times")
        print("--- End report ---")
        


main()
