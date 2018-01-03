# Fusion 360 Object Creation Slowdown Repro

Minimum code to reproduce a problem that currently exists in Fusion 360 where objects are created from script. 
Each new object takes more time to create than the previous object, so creating 100 objects takes significantly 
more than double the time it takes to create 50 objects. Or in other words, when creating 100 objects, the first
50 is much faster than the remaining 50.

According to this post on the Fusion 360 forums, the performance issue has been logged as a defect.
https://forums.autodesk.com/t5/fusion-360-api-and-scripts/creating-cylinders/m-p/7051309#M3226
