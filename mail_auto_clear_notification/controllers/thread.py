# Copyright 2025 Subteno (https://www.subteno.com).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import http
from odoo.addons.mail.controllers.thread import ThreadController
from odoo.http import request


class ThreadController(ThreadController):
    @http.route("/mail/thread/messages", methods=["POST"], type="json", auth="user")
    def mail_thread_messages(
        self, thread_model, thread_id, search_term=None, before=None, after=None, around=None, limit=30
    ):
        domain = [
            ("res_id", "=", int(thread_id)),
            ("model", "=", thread_model),
            ("message_type", "!=", "user_notification"),
        ]
        res = request.env["mail.message"]._message_fetch(
            domain, search_term=search_term, before=before, after=after, around=around, limit=limit
        )
        if not request.env.user._is_public() and request.env.user.has_automatic_clear_on_click:
            res["messages"].set_message_done()
        return {**res, "messages": res["messages"].message_format()}
