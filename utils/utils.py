import os

from utils.formatter import format_description_text

file_path = os.getcwd() + '/tweeted_artworks.txt' 

key_word = 'hearthstone'
not_key_words = ['fanart', 'fan art', 'fan-art']



def check_if_supported(title, desc):
    print(title,'...............................' ,desc)
    supported = False
    for k in not_key_words:
        if title.lower().find(k) >= 0:
            print(title.lower().find(k))
            supported = False
            return supported
        elif desc.lower().find(k) >= 0:
            print(desc.lower().find(k))
            supported = False
            return supported
      
    if title.lower().find(key_word) >= 0:
        print(title.lower().find(key_word))
        supported = True
        return supported
    elif desc.lower().find(key_word) >= 0:
        print(desc.lower().find(key_word))
        supported = True
        return supported 
    else:
        return supported    


def format_artwork(artwork_author, artwork_title, artwork_desc, artwork_url):
    title = '📢 New Official Artwork Spotted 📢'
    t_len = f"{title}\n\n🎨 {artwork_author}\n 🏷️ {artwork_title}\n📜 \n\n🌐 {artwork_url}"
    formatted_artwork_text = format_description_text(artwork_desc, len(t_len))
    text = f"{title}\n\n🎨 {artwork_author}\n 🏷️ {artwork_title}\n📜 {formatted_artwork_text}\n\n🌐 {artwork_url}"

    return text


def check_if_tweeted(artwork_url):
    t = False
    with open(file_path) as f:
        for line in f:
            if line.strip() == artwork_url:
                print(
                    f'artwork with the id "{artwork_url}" already tweeted... ')
                t = True
                break
    return t


def write_artwork_url(artwork_url):
    with open(file_path, "a") as file:
        file.write(artwork_url + '\n')

    return print(f'artwork_url "{artwork_url}" successfully written...')        

# users = []
# with open(os.getcwd() + '/users.txt') as f:
#     for line in f:
#         users.append(line.strip())
#         # print( f'user - "{line.strip()}" successfully appended... ')

#     print(users) 
#     print(len(users))   
