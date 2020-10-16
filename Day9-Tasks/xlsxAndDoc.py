import xlsxwriter
from docx import Document
from db import Database
from model import Patient

class conversion:

    def idXlsx(self):
        """
        Creates xlsx file with patient details of the given id

        PARAMETERS
        -----------------------------------------
        id - patient id to fetch from database

        """
        # Starts session to connect databse and close at end
        with Database.session_scope() as s:  
            id = 1
            p = s.query(Patient).filter(Patient.id == id).first() # Query the databse and returns the patient with given id
            name = str(id)+'_details.xlsx'
            workbook = xlsxwriter.Workbook(name)  # Creates workbook with given name
            worksheet = workbook.add_worksheet()
            col = 0
            for key, value in p.__dict__.items():
                if '_sa_instance_state' in key: # Checking for database object and ignoring it
                    continue
                else:
                    worksheet.write(0, col, key)
                    worksheet.write(1, col, value)
                    col += 1
            workbook.close()

    def idDocx(self):
        """
        Creates docx file with patient details of the given id

        PARAMETERS
        -----------------------------------------
        id - patient id to fetch from database

        """
        # Starts session to connect databse and close at end
        with Database.session_scope() as s:  
            id = 1
            p = s.query(Patient).filter(Patient.id == id).first() # Query the databse and returns the patient with given id
            name = str(id)+'_details.docx'
            document = Document()  # Start's the document
            table = document.add_table(rows=9, cols=2)
            hdr_cells = table.columns[0].cells
            hdr_cells[0].text = 'Id'
            hdr_cells[1].text = 'Name'
            hdr_cells[2].text = 'Address'
            hdr_cells[3].text = 'State'
            hdr_cells[4].text = 'Country'
            hdr_cells[5].text = 'Phone Number'
            hdr_cells[6].text = 'Report'
            row_cells = table.columns[1].cells
            row_cells[0].text = str(p.id)
            row_cells[1].text = p.name
            row_cells[2].text = p.address
            row_cells[3].text = p.state
            row_cells[4].text = p.country
            row_cells[5].text = str(p.phoneNumber)
            row_cells[6].text = p.report
            document.save(name)  # Saves the document with given name


c = conversion()
c.idDocx()
c.idXlsx()