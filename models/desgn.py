from odoo import models, fields, api,_

class DesgnDesgn(models.Model):
     _name="desgn.desgn"
     
     name = fields.Char('name')
     image= fields.Binary("Image", help="Select image here")    
     status = fields.Selection([('neck', 'Neck'), ('color', 'Color'),('caf','Caf'),('pocket','Pocket')], string='Type')

    