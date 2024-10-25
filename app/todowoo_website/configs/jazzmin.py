# Admin Panel
JAZZMIN_SETTINGS = {

    # title of the window (Will default to current_admin_site.site_title
    # if absent or None)
    "site_title": "ToDoWoo",

    # Title on the login screen (19 chars max) (defaults to
    # current_admin_site.site_header if absent or None)
    "site_header": "ToDoWoo",

    # Title on the brand (19 chars max) (defaults to
    # current_admin_site.site_header if absent or None)
    "site_brand": "ToDoWoo",

    # # Logo to use for your site, must be present in static files,
    # # used for brand on top left
    "site_logo": None,

    # # Logo to use for your site, must be present in static files,
    # # used for login form logo (defaults to site_logo)
    # "login_logo": "assets/automagic_developer_logo.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to
    # site_logo if absent (ideally 32x32 px)
    "site_icon": "assets/favicon.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to ToDoWoo :)",

    # Copyright on the footer
    "copyright": "ToDoWoo",

    # List of model admins to search from the search bar, search bar
    # omitted if excluded
    # If you want to use a single search field you dont need to use a list,
    # you can use a simple string
    "search_model": [
    ],

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        # {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {},

        # model admin to link to (Permissions checked against model)
        # {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions
        # checked against models)
        # {"app": "portfolio"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right
    # ("app" url type is not allowed)
    "usermenu_links": [
        # {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": False,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": ['sites'],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [
        'filer.ThumbnailOption'
    ],

    # List of apps (and/or models) to base side menu ordering off of
    # (does not need to contain all apps/models)
    "order_with_respect_to": [
        'todowoo',
        'todowoo.Todo',
        'auth',
        'auth.user',
        'auth.group',
    ],

    # # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "portfolio": [{
    #         "name": "portfolio",
    #         "url": "portfolio",
    #         "icon": "fas fa-comments",
    #         "permissions": ["portfolio.portfolio_home"]
    #     }]
    # },

    # Custom icons for side menu apps/models
    # See shorturl.at/fhzMV
    # https://fontawesome.com/v5/search
    # for the full list of 5.13.0 free icon classes
    "icons": {
        'todowoo': 'fas fa-check-circle',
        'todowoo.Todo': 'fas fa-check-double',
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
    },

    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": 'admin/css/styles.css',

    "custom_js": None,
}
