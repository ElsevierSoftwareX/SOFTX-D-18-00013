from qcobj.qconfigobj import QConfigObj, qLike, val, sumVal, splitPolygons


qcobj = QConfigObj("qcobjExample.cfg", configspec="configspec.cfg")
reg1sec = qcobj['Ingredients']['Regions']['Region1']
reg1Temp = reg1sec['T']

print("This is temperature in Region1: %s" % reg1Temp)
# But we use Kelvin for computing
reg1TempK = reg1Temp.to('K')
print("But we will use this: %s" % reg1TempK)
reg1_t = reg1TempK.magnitude
print("...or better its magnitude: %f" % reg1_t)
# Add some temperature
reg1_t += 10
# Convert this **number** back to its physical quantity as in configspec
newTempQ = qLike(reg1_t, reg1sec, 'T')
print("The result of the computation: %s" % newTempQ)
# Increase voltage by 20 V
sumVal(qcobj, 'voltage', 20.0)
print("The voltage now is: %s" % qcobj['voltage'])

reg2polygons = qcobj['Ingredients']['Regions']['Region2']['polygons']
polylist = splitPolygons(reg2polygons)
print("Number of polygons in region2: %d" % len(polylist))

#from IPython import embed; embed()
print("That's all folks!")
