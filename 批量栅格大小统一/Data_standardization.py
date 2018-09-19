# -*- coding: utf-8 -*-
import arcpy
import os
import traceback

class Data_standardization:
    def __init__(self):
        print(u"程序加载完毕，开始计算")
    def data_standardizationExecute(self, in_raster, out_raster):
        arcpy.CheckOutExtension("spatial")
        
        arcpy.env.extent = arcpy.Extent(self.LEFT, self.BOTTOM, self.RIGHT, self.TOP)
        arcpy.env.outputCoordinateSystem = self.stand_data
        arcpy.env.snapRaster = self.stand_data

        try:
            arcpy.gp.ExtractByMask_sa(in_raster, self.in_mask_data, out_raster)
        except:
            traceback.print_exc()
        print self.LEFT, self.BOTTOM, self.RIGHT, self.TOP
    def data_standardizationMain(self, stand_data, in_mask_data, input_folder, output_folder):
        self.TOP = arcpy.GetRasterProperties_management(stand_data, "TOP")          #—返回范围的顶部值或 Y 最大值 (YMax)。 
        self.LEFT = arcpy.GetRasterProperties_management(stand_data, "LEFT")        #—返回范围的左侧值或 X 最小值 (XMin)。 
        self.RIGHT = arcpy.GetRasterProperties_management(stand_data, "RIGHT")      #—返回范围的右侧值或 X 最大值 (XMax)。 
        self.BOTTOM = arcpy.GetRasterProperties_management(stand_data, "BOTTOM")    #—返回范围的底部值或 Y 最小值 (YMin)。 

        self.stand_data = stand_data
        self.in_mask_data = in_mask_data

        for filelist in os.walk(input_folder):
            for filename in filelist[2]:
                if filename.endswith(".tif"):
                    in_raster = filelist[0] + "\\" + filename
                    current_output_folder = output_folder + "\\" + '\\'.join((filelist[0]).split("\\")[1:])
                    out_raster = current_output_folder + "\\" + filename
                    
                    if os.path.exists(out_raster) == True:
                        os.remove(out_raster)
                    if os.path.exists(current_output_folder) == False:
                        os.makedirs(current_output_folder)
                    
                    print "in_raster:", in_raster
                    print "out_raster:", out_raster
                    self.data_standardizationExecute(in_raster, out_raster)
        
        print u"计算完毕"
if __name__ == "__main__":
    new_data_standardization = Data_standardization()
    stand_data = "E:\\metadata2\\standdata\\qinghai.tif"
    in_mask_data = "E:\\20170917(王兴春检查)\\公用数据\\2010省界面.shp"
    input_folder = "E:\\metadata2"
    output_folder = "E:\\data_standardization"
    new_data_standardization.data_standardizationMain(stand_data, in_mask_data, input_folder, output_folder)
