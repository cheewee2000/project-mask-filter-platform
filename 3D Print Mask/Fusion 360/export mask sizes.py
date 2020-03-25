#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback


def run(context):
    #headWidth, eyeNoseDiagonal, NoseBreadth, sizeNumber
    export('144','36','32','1')
    export('152','39','39','2')
    export('152','37','36','3')
    export('153','43','35','4')
    export('161','40','42','5')
    export('180','40','50','9')

        


    

def export(hw, end, nb, s):

    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        des = adsk.fusion.Design.cast(app.activeProduct)
        userParams = des.userParameters


        userParams.itemByName('HeadWidth').expression = hw
        userParams.itemByName('EyeNoseDiagonal').expression = end
        userParams.itemByName('NoseBreadth').expression = nb
        userParams.itemByName('size').expression = s

        try:
            product = app.activeProduct
            design = adsk.fusion.Design.cast(product)
            exportMgr = design.exportManager
            outDir = "/Users/cwwang/Desktop"

            for comp in design.allComponents:
                for body in comp.bRepBodies:
                    fileName = outDir + "/W1V5 Mask Size "+ s

                    # create stl exportOptions
                    stlExportOptions = exportMgr.createSTLExportOptions(body, fileName)
                    stlExportOptions.sendToPrintUtility = False
                    exportMgr.execute(stlExportOptions)
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))   



