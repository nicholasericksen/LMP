from LMP import LMP


print "============================================================================="
print "Light Measuring Polarimeter (LMP)"
print "A simple program to record values from a photosensor transmitting serial data"
print "============================================================================="
print ""
print "1. Sensor - get a single sensor reading"
print "2. Classical - a classical light measuring polarimeter"
print "3. Stokes - calculate the Stokes params from a txt file"
print ""
mode = raw_input("Enter option #: ")

lmp = LMP()

if (mode == "3"):
    filename = raw_input("Enter filename: ")
    lmp.stokesclassical(filename)
elif (mode == "2"):
    lmp.classical()
else:
    lmp.sensor()
