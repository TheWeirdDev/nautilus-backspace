#!/usr/bin/env python

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import GObject, Nautilus, Gtk


class BackspaceBack(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()

    def get_file_items(self, *args):
        app = Gtk.Application.get_default()
        if not app.get_actions_for_accel("BackSpace"):
            app.set_accels_for_action("slot.back", ["BackSpace"])
        return None
