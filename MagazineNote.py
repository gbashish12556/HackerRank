def checkMagazine(magazine, note):
    dictionary1 = {}
    dictionary2 = {}
    for x in note:
        if x in dictionary1:
            dictionary1[x] += 1
        else:
            dictionary1[x] =1
    for x in magazine:
        if x in dictionary2:
            dictionary2[x] += 1
        else:
            dictionary2[x] =1
    for x in dictionary1:
        if x in dictionary2:
            if dictionary1[x] > dictionary2[x]:
                print("No")
                return
        else:
            print("No")
            return
    print("Yes")

magazine = "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg"
note = "elo lxkvg bg mwz clm w"
magazine = magazine.split(" ")
note = note.split(" ")
checkMagazine(magazine, note)