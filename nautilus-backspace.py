#!/usr/bin/env python

import os, gi
gi.require_version('Nautilus', '4.0')
gi.require_version('Gtk', '4.0')
from gi.repository import GObject, Nautilus, Gtk, Gio, GLib

class BackspaceBack(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()
        pass
    
    def get_file_items(self, *args):
        app = Gtk.Application.get_default()
        app.set_accels_for_action("slot.back", ["BackSpace"])
        return None

