def grade_section1(content):
    count = 0
    i = 0
    while i < len(content) and count < 5:
        if "Enter a word/phrase" in content[i]:
            count += 1
            if 'Palindrome' in content[i] and count < 5:
                i += 1 
            elif 'Not a palindrome' in content[i] and count == 5:
                break
            else:
                return (False, f"Wrong answer for palindrome case {count}")
        i += 1
    return(True, i + 1) 

def grade_section2(content, start):
    i = start 
    j = 0
    k = 0
    expected_books = [
    '0827229534',
    '1571686223',
    'B00005MHUG',
    '055329315X',
    '1841121495'
    ]
    while i < len(content) and k != 5:
        if 'getCartBestSeller' in content[i]:
            if 'The Letters of John Wesley Hardin' not in content[i + 1] and j == 0:
                return (False, "Did return correct best seller")
            elif 'Big Shots: Business the Richard Branson Way' not in content[i + 1] and j == 1:
                return (False, "Did return correct best seller")
            else:
                j += 1 
        elif 'removeFromShoppingCart' in content[i]:
            if expected_books[k] in content[i + 1]:
                k += 1
            else:
                return (False, f"Did not remove correct book at {expected_books[k]}")
        i += 1
    return (True, i + 1) 

def grade_section3(content, start):
    i = start
    count1 = 0
    count2 = 0
    count3 = 0
    while i < len(content):
        if 'Introduce the query to search' in content[i] and count1 == 0:
            i += 1 
            while i < len(content) and count1 < 50 and 'searchBookByInfix Completed' not in content[i]:
                if "Book:" in content[i]:
                    i += 2
                    count1 += 1
                i += 1
            if count1 < 50:
                return (False, "Did not print enough books")
        elif 'Introduce the query to search' in content[i] and count2 == 0 and 'searchBookByInfix Completed' not in content[i]:

            i += 1 
            while i < len(content) and count2 < 4:
                if "Book:" in content[i] and "World of Pa" in content[i+1]:
                    i += 2
                    count2 += 1
                i += 1
            if count2 < 4: 
                return (False, "Did not print enough books")
        elif 'Introduce the query to search' in content[i] and count3 == 0 and 'searchBookByInfix Completed' not in content[i]:

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
    section3 = grade_section3(content, section2[1])
    if not section3[0]:
        fd.close()
        return section3[1]
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
