from odoo import api, models, fields
from odoo.exceptions import ValidationError, UserError
import logging
_logger = logging.getLogger(__name__)

class CustomerInformation(models.Model):
    _name = 'customer.information'
    _description = 'Customer Information'

    first_name = fields.Char(string="पहिलो नाम: ")
    middle_name = fields.Char(string="विचको नाम: ")
    last_name = fields.Char(string="आन्तिमको नाम: ")
    district = fields.Char(string="जिल्ला: ")
    local_level_type = fields.Selection([
        ('metropolitian-city', 'Metropolitian City'),
        ('municipality', 'Municipality'),
        ('rural-municipality', 'Rural Municipality')
    ], string="पालिका: ")
    local_level_type_name = fields.Char(string="नाम: ")
    ward_number = fields.Integer(string="वडा नं: ")
    state = fields.Selection([
        ('one', '1'),
        ('two', '2'), 
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
    ], string="प्रदेश: ")
    nationality = fields.Char(string="राष्ट्रियता: ", default="Nepali")
    national_id = fields.Char(string="राष्ट्रिय परिचय पत्र नं: ")
    citizenship = fields.Char(string="नागरिकता नं: ")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="लिङ्ग: ", default="male")
    organization_name = fields.Char(string="फर्म/संस्थाको नाम:")
    selling_item = fields.Selection([
        ('seed_sowing', 'बिऊ विजन'),
        ('fertilizer', 'मल'),
        ('insecticide', 'विषादी'),
        ('agricultural_tools', 'कृषि औजार')
    ], string="कारोबार गर्ने मुख्य सामान: ", default="seed_sowing")
    type_of_business = fields.Selection([
        ('wholesale', 'थोक'),
        ('retail', 'खुद्रा'),
        ('import', 'आयात'),
        ('production', 'उत्पादन')
    ], string="व्यवसायको किसिम: ", default="wholesale")
    trade_location = fields.Char(string="कारोबारको स्थायी ठेगाना: ")
    phone_number = fields.Char(string="फोन नं: ")
    fax = fields.Char(string="फ्याक्स: ")
    mobile_number = fields.Char(string="मो.नं: ")
    email = fields.Char(string="इमेल ठेगाना: ")
    company_owner_name = fields.Char(string="फर्म धनी (कम्पनीको मालिक वा मुख्य  व्यक्ति को नाम): ")
    manager_name = fields.Char(string="प्रबन्धकको नाम: ")
    office_registered = fields.Char(string="नेपाल सरकारमा दर्ता भएको कार्यालय: ")
    factory = fields.Selection([
        ('domestic', 'घरेलु'),
        ('administration','प्रशासन'),
        ('others','आदी')
    ], string="उद्योक: ", default="domestic")
    registered_number = fields.Integer(string="दर्ता नं: ")
    registered_date = fields.Date(string="दर्ता मिति: ")
    branch_location = fields.Char(string="शाखा/उपशाखा (भए सो को ठेगाना खुलाउने): ")
    total_employee = fields.Integer(string="हाल कार्यरत कर्मचारी संख्या: ")
    last_renewal_date = fields.Date(string="आन्तिम नविकरण भएको मिति: ")
    form_number = fields.Char(string="फारम नं: ")
    membership_number = fields.Char(string="सदस्यता नं: ")
    status = fields.Selection([
        ('draft', 'Draft'),
        ('prepared', 'Preprared'),
        ('checked', 'Checked'),
        ('approved', 'Approved')
    ], string="State", default="draft")

    def action_confirm(self):
        _logger.info("Action Confirm Button Clicked")
        for rec in self:
            if rec.status == 'draft':
                rec.update({
                    'status': 'prepared'
                })
            else:
                _logger.info("N/A")

    def action_checked(self):
        _logger.info("Action Checked Button Clicked")
        for rec in self:
            if rec.status == 'prepared':
                rec.update({
                    'status': 'checked'
                })
            else:
                _logger.info("N/A")
    
    def action_approved(self):
        _logger.info("Action Approved Button Clicked")
        for rec in self:
            if rec.status == 'checked':
                rec.update({
                    'status': 'approved'
                })
            else:
                _logger.info("N/A")