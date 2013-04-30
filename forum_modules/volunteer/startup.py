from forum.modules import ui
from django.utils.translation import ugettext as _


ui.register(ui.FOOTER_LINKS,
    ui.Link(_('volunteer'), '/volunteer'),
)

ui.register(ui.HEADER_LINKS,
    ui.Link(_('volunteer'), '/volunteer'),
)
