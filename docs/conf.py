# -*- coding: utf-8 -*-
#
# -- General configuration ----------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'sphinx theme for reveal.js'
copyright = u'2014, tell-k'

version = '0.3.5'

# -- Options for HTML output --------------------------------------

extensions = ['sphinxjp.themes.revealjs']
html_theme = 'revealjs'
html_use_index = False

# -- HTML theme options for `revealjs` style ---------------------

html_theme_options = {
    # Set the lang attribute of the html tag. Defaults to 'ja'
    'lang': 'en',

    # The 'normal' size of the presentation, aspect ratio will be preserved
    # when the presentation is scaled to fit different resolutions
    'width': 960,
    'height': 700,

    # Factor of the display size that should remain empty around the content
    'margin': 0.1,

    # Bounds for smallest/largest possible scale to apply to content
    'min_scale': 0.2,
    'max_scale': 1.0,

    # Display controls in the bottom right corner
    'controls': True,

    # Display a presentation progress bar
    'progress': True,

    # Set default timing of 2 minutes per slide
    'default_timing': 120,

    # Display the page number of the current slide
    'slide_number': False,

    # Push each slide change to the browser history
    'history': True,

    # Enable keyboard shortcuts for navigation
    'keyboard': True,

    # Enable the slide overview mode
    'overview': True,

    # Vertical centering of slides
    'center': True,

    # Enables touch navigation on devices with touch input
    'touch': True,

    # Loop the presentation
    'loop': False,

    # Change the presentation direction to be RTL
    'rtl': False,

    # Randomizes the order of slides each time the presentation loads
    'shuffle': False,

    # Turns fragments on and off globally
    'fragments': True,

    # Flags if the presentation is running in an embedded mode,
    # i.e. contained within a limited portion of the screen
    'embedded': False,

    # Flags if we should show a help overlay when the questionmark
    # key is pressed
    'help': True,

    # Flags if speaker notes should be visible to all viewers
    'show_notes': False,

    # Global override for autolaying embedded media (video/audio/iframe)
    # - : Media will only autoplay if data-autoplay is present
    # - True: All media will autoplay, regardless of individual setting
    # - False: No media will autoplay, regardless of individual setting
    #'autoPlayMedia': '',

    # Number of milliseconds between automatically proceeding to the
    # next slide, disabled when set to 0, this value can be overwritten
    # by using a data-autoslide attribute on your slides
    'auto_slide': 0,

    # Stop auto-sliding after user input
    'auto_slide_stoppable': True,

    # Use this method for navigation when auto-sliding
    'auto_slide_method': 'Reveal.navigateNext',

    # Enable slide navigation via mouse wheel
    'mouse_wheel': False,

    # Hides the address bar on mobile devices
    'hide_address_bar': True,

    # Opens links in an iframe preview overlay
    'preview_links': False,

    # Transition style (default(=convex)/none/fade/slide/concave/zoom)
    'transition': 'default',

    # Transition speed (default/fast/slow)
    'transition_speed': 'default',

    # Transition style for full page slide backgrounds (default(=convex)/none/fade/slide/concave/zoom)
    'background_transition': 'default',

    # Theme (black/white/league/beige/sky/night/serif/simple/solarized)
    'theme': 'beige',

    # Parallax background image
    # CSS syntax, e.g. 'a.jpg'
    #'parallax_background_image': '_static/bg.jpg',

    # Parallax background size
    # CSS syntax, e.g. '3000px 2000px'
    #'parallax_background_size': '2000px 900px',

    # Number of pixels to move the parallax background per slide
    # - Calculated automatically unless specified
    # - Set to 0 to disable movement along an axis
    #'parallax_background_horizontal': None,
    #'parallax_background_vertical': None,

    # The display mode that will be used to show slides
    'display': 'block'

    # Enable plugin javascript for reveal.js
    # "plugin_list": [
    #  "_static/plugin/search/search.js",
    #  "_static/plugin/remotes/remotes.js"
    # ],

    # config for Multiplexing
    # "multiplex": {
    #   # None so the clients do not have control of the master presentation
    #   "secret": None,
    #   "id": '1ea875674b17ca76', # id, obtained from socket.io server
    #   "url": 'example.com:80' # Location of your socket.io server
    # },

    # config for MathJax
    # "math": {
    #     "mathjax": 'http://cdn.mathjax.org/mathjax/latest/MathJax.js',
    #     # See http://docs.mathjax.org/en/latest/config-files.html
    #     "config": 'TeX-AMS_HTML-full'
    # },

    # loading custom js after RevealJs.initialize.
    # "customjs": "mysettings.js",
}

html_static_path = ['_static']
