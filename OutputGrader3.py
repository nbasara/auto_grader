def grade_section1(content):
    count = 0
    i = 0
    while i < len(content) and count < 5:
        if "Introduce the book key:" in content[i]:
            count += 1
            if 'Book not found.' in content[i] and count == 1:
                i += 1 
            elif 'Added title: The Eel' in content[i] and count == 2:
                i += 1 
            elif 'Added title: The World of Pooh' in content[i] and count == 3:
                i += 1 
            elif 'Added title: Big Shots:' in content[i] and count == 4:
                i += 1 
            elif 'Added title: Reckless' in content[i] and count == 5:
                i += 1 
            else:
                return (False, "Wrong book was added to cart")
        i += 1
    return(True, i + 1) 

def grade(): 
    fd = open('output.txt', 'r')
    content = fd.readlines()
    section1 = grade_section1(content)
    if not section1[0]:
        fd.close()
        return section1[1]
    fd.close()
    return "pass"

if __name__ == '__main__':
    score = grade() 
    if score == 'pass':
        fd = open("reason.txt", 'w')
        fd.write(score)
        fd.close()
        exit(0)
    else:
        fd = open("reason.txt", 'w')
        fd.write(score)
        fd.close()
        exit(1)
