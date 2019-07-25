# -*- coding: utf-8 -*-

from odoo import models, fields, api

class xmarts_sdp(models.Model):
    _inherit = 'sdp'

    currency_id = fields.Many2one("res.currency",string="Currency", readonly=True)
    
    amount_total = fields.Monetary(string='Total', store=True, readonly=True, compute='_to', track_visibility='always', track_sequence=6)
    
    @api.depends('subtotal')
    def _to(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            order.update({
                 'amount_total': order.subtotal
            })