filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = filenames
print(filenames)
for i,v in enumerate(newfilenames):
    if v.split(".")[1] == "hpp":
        idx = v.find(".")
        filenames[i] =filenames[i][:idx+1] +"h"


print(filenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]