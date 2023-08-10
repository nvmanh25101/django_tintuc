APP_VALUE_LAYOUT_DEFAULT = 'list'
APP_VALUE_STATUS_DEFAULT = 'draft'
APP_VALUE_LAYOUT_CHOICES = (
    ('list', 'List'),
    ('grid', 'Grid'),
)
APP_VALUE_STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

ADMIN_SRC_CSS = {'all': ('my_admin/css/custom.css',)}
ADMIN_SRC_JS = ('my_admin/js/jquery-3.6.4.min.js', 'my_admin/js/slugify.js', 'my_admin/js/general.js')

ADMIN_SITE_HEADER = 'Admin'