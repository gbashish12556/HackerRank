def count_substring(string, sub_string):
    count = 0
    lensub = len(sub_string)
    lenstring = len(string)
    for i in range(lenstring-lensub+1):
        if string[i:lensub+i] == sub_string:
            count +=1
    return count

string = "ABCDCDC"
sub_string = "CDC"
count_substring(string,sub_string)