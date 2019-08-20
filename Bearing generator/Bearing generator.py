#Author-Daniel Aguirre
#Description-A script for making custom made bearings with a 3D printer and some BB balls

import adsk.core, adsk.fusion, adsk.cam, traceback

import math

# Bearings variables

_units = "mm"

h = 10
di = 9
do = 30
dbb = 7
dbb_extract = 2
wgap = 1.5


def run(context):
    ui = None
    try:    
        global h, di, do, dbb, dbb_extract, wgap
        # Check values bigger than 0
        ## TO DO
        
        # Check there is enough space for the balls
        if ((do-di)/2 <= dbb):
            thickness = 2
            do = 2*(dbb + 2*thickness) + di
            if ui:
                ui.messageBox("Bearing's width too thin. Modified Outside diameter to: " + str(do))
                
        if (h <= dbb):
            thickness = 0.2
            h = h + 2*thickness
            if ui:
                ui.messageBox("Bearing's width too thin. Modified Thickness to: " + str(h))
    
        # Convert to "cm" (because scripts works with cm)    
        if _units == "mm": # 1mm -> 0.1cm 
            scale = 0.1 
        elif _units == "m": # 1m -> 100cm 
            scale = 100
        else:
            scale = 1
       
        
            
        h = h*scale
        di = di*scale
        do = do*scale
        dbb = dbb*scale
        dbb_extract = dbb_extract*scale
        wgap = wgap*scale

        
        app = adsk.core.Application.get()
        ui = app.userInterface        
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        
        design = app.activeProduct
        
        # Get the root component of the active design.
        rootComp = design.rootComponent
        
        # Get extrude and revolve features
        extrudes = rootComp.features.extrudeFeatures 
        revolves = rootComp.features.revolveFeatures
        
        # Create basic construction planes.
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane        
        yzPlane = rootComp.yZConstructionPlane
        
        
        
        # STEP 1: Draw inner and outer diameters
        sketch1 = sketches.add(xyPlane)
        circles = sketch1.sketchCurves.sketchCircles
        circle1 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), di/2)
        circle2 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), do/2)
        
        # STEP 2: Extrude (create) previous circles   
        prof1 = sketch1.profiles.item(1)
        extInput1 = extrudes.createInput(prof1, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extInput1.setSymmetricExtent(adsk.core.ValueInput.createByReal(h/2), False)
        extrude1 = extrudes.add(extInput1)
        
        # STEP 3: Draw gap circles     
        dm = (di + do)/2        
        sketch2 = sketches.add(xyPlane)
        circles = sketch2.sketchCurves.sketchCircles
        circle3 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), (dm + wgap/2)/2)
        circle4 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), (dm - wgap/2)/2)
        circle5 = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), dm/2)
        circle5.isConstruction = True
        
        # STEP 4: Extrude (cut) with previous circles
        prof2 = sketch2.profiles.item(0)        
        extInput2 = extrudes.createInput(prof2, adsk.fusion.FeatureOperations.CutFeatureOperation)
        extInput2.setSymmetricExtent(adsk.core.ValueInput.createByReal(h/2), False)
        extrude2 = extrudes.add(extInput2)        
        
        # STEP 5: Draw BB circle
        sketch3 = sketches.add(yzPlane)
        circles = sketch3.sketchCurves.sketchCircles
        circle6 = circles.addByCenterRadius(adsk.core.Point3D.create(0, dm/2, 0), dbb/2)
        
        # STEP 6: Revolute (cut) with previous circles        
        # Draw a line to use as the axis of revolution.
        lines = sketch3.sketchCurves.sketchLines
        axisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-h/2, 0, 0), adsk.core.Point3D.create(h/2, 0, 0))
        axisLine.isConstruction = True
        
        prof3 = sketch3.profiles.item(0)        
        revInput = revolves.createInput(prof3, axisLine, adsk.fusion.FeatureOperations.CutFeatureOperation)
        angle = adsk.core.ValueInput.createByReal(2*math.pi)
        revInput.setAngleExtent(False, angle) 
        revolute1 = revolves.add(revInput)        
        
        # STEP 7: Draw insertion circle
        sketch4 = sketches.add(xyPlane)
        circles = sketch4.sketchCurves.sketchCircles  
        circle7 = circles.addByCenterRadius(adsk.core.Point3D.create(0, dm/2, 0), dbb_extract/2)
        circle7 = circles.addByCenterRadius(adsk.core.Point3D.create(0, dm/2, 0), dbb/2)
        
        # STEP 8: Extrude (cut) with previous circles
        prof4 = sketch4.profiles.item(0)        
        extInput3 = extrudes.createInput(prof4, adsk.fusion.FeatureOperations.CutFeatureOperation)
        extInput3.setSymmetricExtent(adsk.core.ValueInput.createByReal(h/2), False)
        extrude3 = extrudes.add(extInput3)
        
        prof5 = sketch4.profiles.item(1)        
        extInput4 = extrudes.createInput(prof5, adsk.fusion.FeatureOperations.CutFeatureOperation)
        extInput4.setOneSideExtent(adsk.fusion.ThroughAllExtentDefinition.create(), adsk.fusion.ExtentDirections.PositiveExtentDirection)
        extrude4 = extrudes.add(extInput4)   
        
       
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
            
            