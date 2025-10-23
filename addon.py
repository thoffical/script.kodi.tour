import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

# Set a string variable to use 
line1 = "Welcome to Kodi!, Select OK to start"

# Launch a dialog box in kodi showing the string variable 'line1' as the contents
xbmcgui.Dialog().ok(addonname, line1)

# Set a string variable to use 
line2 = "Kodi is a free open source software licensed under the GPL License"

# Launch a dialog box in kodi showing the string variable 'line1' as the contents
xbmcgui.Dialog().ok(What is Kodi, line2)
