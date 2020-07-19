<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" minScale="1e+08" styleCategories="AllStyleCategories" maxScale="inf" version="3.10.4-A Coruña">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="identify/format" value="Value"/>
  </customproperties>
  <pipe>
    <rasterrenderer classificationMin="-3.60576e-05" alphaBand="0" type="singlebandpseudocolor" opacity="1" band="1" classificationMax="1.60022e-05">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>CumulativeCut</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader colorRampType="INTERPOLATED" classificationMode="1" clip="0">
          <item label="100" value="-0.0001" color="#ca0020" alpha="255"/>
          <item label="50" value="-5e-05" color="#f4a582" alpha="255"/>
          <item label="0" value="0" color="#f7f7f7" alpha="255"/>
          <item label="-50" value="5e-05" color="#92c5de" alpha="255"/>
          <item label="-100" value="0.0001" color="#0571b0" alpha="255"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation colorizeStrength="100" grayscaleMode="0" colorizeBlue="128" colorizeRed="255" saturation="0" colorizeOn="0" colorizeGreen="128"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
