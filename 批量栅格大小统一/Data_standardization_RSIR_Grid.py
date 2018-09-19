# -*- coding: utf-8 -*-
import arcpy
import os
import traceback

class Data_standardization_RSIR_Grid:
    def __init__(self):
        print(u"程序加载完毕，开始计算")
    def Data_standardization_RSIR_GridExecute(self, in_raster, out_raster, filename):
        arcpy.CheckOutExtension("spatial")
        
        mem_path = "in_memory"
        
        arcpy.env.extent = arcpy.Extent(self.LEFT, self.BOTTOM, self.RIGHT, self.TOP)
        arcpy.env.outputCoordinateSystem = self.stand_data
        arcpy.env.snapRaster = self.stand_data
        
        try:
            arcpy.Resample_management(in_raster, os.path.join(mem_path, filename), "250 250", "NEAREST")
            arcpy.gp.ExtractByMask_sa(os.path.join(mem_path, filename), self.in_mask_data, out_raster)
            try:
                arcpy.Delete_management(os.path.join(mem_path, filename))
            except:
                traceback.print_exc()
        except:
            traceback.print_exc()

                
        print self.LEFT, self.BOTTOM, self.RIGHT, self.TOP
    def Data_standardization_RSIR_GridMain(self, stand_data, in_mask_data, input_folder, output_folder):
        print "input_folder is:%s" % input_folder
        
        self.TOP = arcpy.GetRasterProperties_management(stand_data, "TOP")          #—返回范围的顶部值或 Y 最大值 (YMax)。 
        self.LEFT = arcpy.GetRasterProperties_management(stand_data, "LEFT")        #—返回范围的左侧值或 X 最小值 (XMin)。 
        self.RIGHT = arcpy.GetRasterProperties_management(stand_data, "RIGHT")      #—返回范围的右侧值或 X 最大值 (XMax)。 
        self.BOTTOM = arcpy.GetRasterProperties_management(stand_data, "BOTTOM")    #—返回范围的底部值或 Y 最小值 (YMin)。 

        self.stand_data = stand_data
        self.in_mask_data = in_mask_data

        file_list = ["hdr.adf"]
        
        for filelist in os.walk(input_folder):
            for filename in filelist[2]:
                if filename in file_list:
                    in_raster = filelist[0]
                    out_raster = output_folder + "\\" + '\\'.join((filelist[0]).split("\\")[1:])
                    
                    if os.path.exists(out_raster) == True:
                        arcpy.DeleteRasterCatalogItems_management(out_raster)
                    if os.path.exists('\\'.join(out_raster.split("\\")[:-1])) == False:
                        os.makedirs('\\'.join(out_raster.split("\\")[:-1]))
                    
                    print "in_raster:", in_raster
                    print "out_raster:", out_raster
                    self.Data_standardization_RSIR_GridExecute(in_raster, out_raster, in_raster.split("\\")[-1])
        
        print u"计算完毕"
if __name__ == "__main__":
    new_Data_standardization_RSIR_Grid = Data_standardization_RSIR_Grid()
    
    stand_data = "E:\\metadata2\\standdata\\qinghai.tif"
    in_mask_data = "E:\\20170917(王兴春检查)\\公用数据\\2010省界面.shp"
    input_folder = "F:\\data\\20171004"
    output_folder = "F:\\data_standardization"
    
    new_Data_standardization_RSIR_Grid.Data_standardization_RSIR_GridMain(stand_data, in_mask_data, input_folder, output_folder)
