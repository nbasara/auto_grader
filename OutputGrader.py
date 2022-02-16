def grade_section1(content):
    i = 0
    j = 0
    k = 0
    expected_books = [
    '0827229534',
    'B00005MHUG',
    '055329315X',
    '1841121495',
    '1571686223'
    ]
    while i < len(content) and k != 5:
        if 'Introduce the index to add' in content[i]:
            if expected_books[j] in content[i + 1]:
                j += 1
            else:
                return (False, f"Did not add correct book at {expected_books[j]}")
        elif 'removeFromShoppingCart' in content[i]:
            if expected_books[k] in content[i + 1]:
                k += 1
            else:
                return (False, f"Did not remove correct book at {expected_books[k]}")
        i += 1
    return (True, i + 1) 

def grade_section2(content, start):
    i = start
    count1 = 0
    count2 = 0
    count3 = 0
    while i < len(content):
        if 'Introduce the query to search' in content[i] and count1 == 0:
            i += 1 
            while i < len(content) and count1 < 50:
                if "Book:" in content[i]:
                    i += 2
                    count1 += 1
                i += 1
            if count1 < 50:
                return (False, "Did not print enough books")
        elif 'Introduce the query to search' in content[i] and count2 == 0:
            i += 1 
            while i < len(content) and count2 < 4:
                if "Book:" in content[i] and "World of Pa" in content[i+1]:
                    i += 2
                    count2 += 1
                i += 1
            if count2 < 4: 
                return (False, "Did not print enough books")
        elif 'Introduce the query to search' in content[i] and count3 == 0:
            i += 1 
            while i < len(content) and count3 < 1:
                if "Book:" in content[i] and "Tears of the Wo" in content[i+1]:
                    i += 2
                    count3 += 1
                i += 1
            if count3 < 1: 
                return (False, "Did not print enough books")
        elif 'Book:' in content[i]:
            return (False, 'Printed too many books')
        i += 1 
    return (True, "pass")

def grade(): 
    fd = open('output.txt', 'r')
    content = fd.readlines()
    section1 = grade_section1(content)
    if not section1[0]:
        fd.close()
        return section1[1]
    section2 = grade_section2(content, section1[1])
    if not section2[0]:
        fd.close()
        return section2[1]
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
