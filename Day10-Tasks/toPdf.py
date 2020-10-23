import os
import pythoncom
import win32com.client
from pywintypes import com_error
from docx2pdf import convert

class Service:

    def xlsxToPdf(self, fileToBeConverted):
        pythoncom.CoInitialize()
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = False
        
        WB_PATH = os.path.abspath(fileToBeConverted)
        PATH_TO_PDF = WB_PATH[:-5] + '_worksheet.pdf'
            
        # Open
        wb = excel.Workbooks.Open(WB_PATH)
            
        try:
            # Save
            wb.ActiveSheet.ExportAsFixedFormat(0, PATH_TO_PDF)
        except com_error as e:
            print('failed.')
        finally:
            wb.Close()
            excel.Quit()

    def docxToPdf(self,fileToBeConverted):
        
        # Path to original DOCX file
        WB_PATH = os.path.abspath(fileToBeConverted)
        
        # Converted pdf file name
        PATH_TO_PDF = WB_PATH[:-5] + '_info.pdf'
        #COM initializing to access WORD Application
        pythoncom.CoInitialize()
        convert(WB_PATH, PATH_TO_PDF)


s = Service()
s.xlsxToPdf("1.xlsx")
s.docxToPdf("1.docx")