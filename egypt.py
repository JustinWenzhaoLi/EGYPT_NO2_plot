

from qgis.core import QgsProject
# Get the project instance
project = QgsProject.instance()
project.read('/Users/wenzhaoshanda/Documents/COVID19_NO2/EGYPT.qgs')
## 
fi = 'EGYPT_June_07_2020'
fp = '/Users/wenzhaoshanda/Downloads/files/'
path_to_tif = fp + fi + '.tif'
fn = QFileInfo(path_to_tif)
fname = fn.baseName()
layer1 = QgsRasterLayer(path_to_tif, fname)
layer1.loadNamedStyle('/Users/wenzhaoshanda/Documents/COVID19_NO2/colorbar.qml')

root = QgsProject.instance().layerTreeRoot()
root.addLayer(layer1)

composerTitle = 'no2Egypt'
projectLayoutManager = project.layoutManager()
l_out = projectLayoutManager.layoutByName(composerTitle)
## iface.openLayoutDesigner(layout=l_out)
exporter = QgsLayoutExporter(l_out)
imageSettings = exporter.ImageExportSettings()
imageSettings.dpi = 300
imageSettings.cropToContents=True
exporter.exportToImage(fp + fi + '.png', imageSettings)

root.removeLayer(layer1)
#################################

## 
fi = 'EGYPT_June_05_June_06_2020'
fp = '/Users/wenzhaoshanda/Downloads/files/'
path_to_tif = fp + fi + '.tif'
fn = QFileInfo(path_to_tif)
fname = fn.baseName()
layer1 = QgsRasterLayer(path_to_tif, fname)
layer1.loadNamedStyle('/Users/wenzhaoshanda/Documents/COVID19_NO2/colorbar.qml')

root = QgsProject.instance().layerTreeRoot()
root.addLayer(layer1)

composerTitle = 'no2Egypt'
projectLayoutManager = project.layoutManager()
l_out = projectLayoutManager.layoutByName(composerTitle)
## iface.openLayoutDesigner(layout=l_out)
exporter = QgsLayoutExporter(l_out)
imageSettings = exporter.ImageExportSettings()
imageSettings.dpi = 300
imageSettings.cropToContents=True
exporter.exportToImage(fp + fi + '.png', imageSettings)

root.removeLayer(layer1)




from qgis.core import QgsProject
# Get the project instance
project = QgsProject.instance()
project.read('/Users/wenzhaoshanda/Documents/COVID19_NO2/EGYPT.qgs')
## 
fi = 'EGYPT_June_08_2020'
fp = '/Users/wenzhaoshanda/Downloads/files/'
path_to_tif = fp + fi + '.tif'
fn = QFileInfo(path_to_tif)
fname = fn.baseName()
layer1 = QgsRasterLayer(path_to_tif, fname)
layer1.loadNamedStyle('/Users/wenzhaoshanda/Documents/COVID19_NO2/colorbar.qml')

root = QgsProject.instance().layerTreeRoot()
root.addLayer(layer1)

composerTitle = 'no2Egypt'
projectLayoutManager = project.layoutManager()
l_out = projectLayoutManager.layoutByName(composerTitle)
## iface.openLayoutDesigner(layout=l_out)
exporter = QgsLayoutExporter(l_out)
imageSettings = exporter.ImageExportSettings()
imageSettings.dpi = 300
imageSettings.cropToContents=True
exporter.exportToImage(fp + fi + '.png', imageSettings)

root.removeLayer(layer1)
#################################

## 
fi = 'EGYPT_June_07_June_08_2020'
fp = '/Users/wenzhaoshanda/Downloads/files/'
path_to_tif = fp + fi + '.tif'
fn = QFileInfo(path_to_tif)
fname = fn.baseName()
layer1 = QgsRasterLayer(path_to_tif, fname)
layer1.loadNamedStyle('/Users/wenzhaoshanda/Documents/COVID19_NO2/colorbar.qml')

root = QgsProject.instance().layerTreeRoot()
root.addLayer(layer1)

composerTitle = 'no2Egypt'
projectLayoutManager = project.layoutManager()
l_out = projectLayoutManager.layoutByName(composerTitle)
## iface.openLayoutDesigner(layout=l_out)
exporter = QgsLayoutExporter(l_out)
imageSettings = exporter.ImageExportSettings()
imageSettings.dpi = 300
imageSettings.cropToContents=True
exporter.exportToImage(fp + fi + '.png', imageSettings)

root.removeLayer(layer1)

#################################
#################################
####### DIFF ####################
#################################
#################################

from qgis.core import QgsProject
# Get the project instance
project = QgsProject.instance()
project.read('/Users/wenzhaoshanda/Documents/COVID19_NO2/EGYPT_diff.qgs')
## 
fi = 'EGYPT_June_05to06_June_07to08__2020__diff'
fp = '/Users/wenzhaoshanda/Downloads/files/'
path_to_tif = fp + fi + '.tif'
fn = QFileInfo(path_to_tif)
fname = fn.baseName()
layer1 = QgsRasterLayer(path_to_tif, fname)
layer1.loadNamedStyle('/Users/wenzhaoshanda/Documents/COVID19_NO2/colorbar_diff.qml')

root = QgsProject.instance().layerTreeRoot()
root.addLayer(layer1)

composerTitle = 'no2Egypt_diff'
projectLayoutManager = project.layoutManager()
l_out = projectLayoutManager.layoutByName(composerTitle)
## iface.openLayoutDesigner(layout=l_out)
exporter = QgsLayoutExporter(l_out)
imageSettings = exporter.ImageExportSettings()
imageSettings.dpi = 300
imageSettings.cropToContents=True
exporter.exportToImage(fp + fi + '.png', imageSettings)

root.removeLayer(layer1)
#################################

## 
fi = 'EGYPT_June_07_June_08_2020__diff'
fp = '/Users/wenzhaoshanda/Downloads/files/'
path_to_tif = fp + fi + '.tif'
fn = QFileInfo(path_to_tif)
fname = fn.baseName()
layer1 = QgsRasterLayer(path_to_tif, fname)
layer1.loadNamedStyle('/Users/wenzhaoshanda/Documents/COVID19_NO2/colorbar_diff.qml')

root = QgsProject.instance().layerTreeRoot()
root.addLayer(layer1)

composerTitle = 'no2Egypt_diff'
projectLayoutManager = project.layoutManager()
l_out = projectLayoutManager.layoutByName(composerTitle)
## iface.openLayoutDesigner(layout=l_out)
exporter = QgsLayoutExporter(l_out)
imageSettings = exporter.ImageExportSettings()
imageSettings.dpi = 300
imageSettings.cropToContents=True
exporter.exportToImage(fp + fi + '.png', imageSettings)

root.removeLayer(layer1)
#################################


