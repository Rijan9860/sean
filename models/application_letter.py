from odoo import api, models, fields
from odoo.exceptions import ValidationError

class ApplicationLetter(models.Model):
    _name = 'application.letter'
    _description = 'Application letter'

    company_name = fields.Char(string="कम्पनीको नाम: ")
    area = fields.Char(string="क्षेत्र: ")
    province = fields.Boolean(string="प्रदेश: ")
    zone = fields.Char(string="अञ्चल: ")
    district = fields.Char(string="जिल्ला: ")
    local_level_type = fields.Selection([
        ('metropolitian-city', 'Metropolitian City'),
        ('municipality', 'Municipality'),
        ('rural-municipality', 'Rural Municipality')
    ], string="पालिका: ")
    local_level_type_name = fields.Char(string="नाम: ")
    contact_number = fields.Char(string="सम्पर्क नम्बर: ")
    mobile_number = fields.Char(string="मोवाईल नं: ")
    org_reg_certificate = fields.Selection([
        ('domestic', 'घरेलु'),
        ('district_administration_office', 'जि.प्र.का.'),
        ('department_of_commerce', 'वाणिज्य विभाग'),
        ('other', 'अन्य')
    ], string="संस्था दर्ता प्रमाणपत्र: ", default="domestic")
    seed_liscense = fields.Char(string="बीउ विजन ईजाजत पत्र: ", default="जिल्ला कृषि विकास कार्यालय")
    internal_revenue_registration = fields.Boolean(string="आन्तरिक राजस्व दर्ता (पान नं) प्रमाणपत्र: ")
    citizenship_certificate = fields.Boolean(string="ननागरिकता प्रमाण पत्र: ")
    member_of_sean = fields.Selection([
        ('yes', 'छ'),
        ('no', 'छैन')
    ], string='नेपालबीउ  व्यवसाही संघ आवद्धता: ')
    membership_date = fields.Date(string="आवद्धता मिति: ")
    membership_renewal_date = fields.Date(string="आवद्धता नविकरण मिति: ")
    membership_renewed_since = fields.Date(string="संघमा आवद्धता नविकरण विगतदेखि भएको/नभएको (मिति): ")
    organization_firm_id = fields.Char(string="संस्था /फर्म आई.डी.नं: ")
    membership_certificate_isssued = fields.Boolean(string="आवद्धता  प्रमाण पत्र दिएको/नदिएको: ")