def concatenate(s1: str, s2: str) -> str:
    concate = s1+s2
    if len(concate) > 10:
        return "Too long!"
    return concate




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
