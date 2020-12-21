passwordlist = []

f = open('day2input.txt', 'r')

for line in f:
    clean_num = line.strip('\\\n')
    passwordlist.append(clean_num)


def helper(pw):
    pwcomp = pw.split(" ")[0:3]
    nums = pwcomp[0]
    letter = pwcomp[1][0]
    password = pwcomp[2]
    return nums, letter, password


def part1():
    total = 0
    for pw in passwordlist:
        freqs, letter, password = helper(pw)
        minfreq = int(freqs[:freqs.index("-")])
        maxfreq = int(freqs[freqs.index("-") + 1:])
        inpw = password.count(letter)
        if minfreq <= inpw <= maxfreq:
            total += 1
    return total


def part2():
    total = 0
    for pw in passwordlist:
        inds, letter, password = helper(pw)
        minind = int(inds[:inds.index("-")]) -1
        maxind = int(inds[inds.index("-") + 1:])-1
        if (password[minind] == letter) is not (password[maxind] == letter):
            total += 1
    return total


print(part1())
print(part2())