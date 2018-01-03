#Author-Roger Cheng
#Description-Minimum code to reproduce issue where each new object takes longer to create than the previous one.

import adsk.core, adsk.fusion, adsk.cam, traceback

arraySize = 8 # Will extrude arraySize^2 objects

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

        # adsk.fusion.Design.cast(app.activeProduct).designType = adsk.fusion.DesignTypes.DirectDesignType # Uncomment to turn off tracking timeline

        rootComp = adsk.fusion.Design.cast(app.activeProduct).rootComponent
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        extrudeDistance = adsk.core.ValueInput.createByReal(1)

        rangeX = range(1-arraySize, arraySize, 2)
        rangeY = range(1-arraySize, arraySize, 2)

        for nowX in rangeX:
            for nowY in rangeY:
                sketch.sketchCurves.sketchCircles.addByCenterRadius(
                    adsk.core.Point3D.create(nowX, nowY, 0), 0.5)

                rootComp.features.extrudeFeatures.addSimple(
                    sketch.profiles[-1],
                    extrudeDistance,
                    adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

                adsk.doEvents()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
