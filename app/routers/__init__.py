from .kpi_router import kpi_router
from .tourists_router import tourists_router
from .regions_router import regions_router
from .demographics_router import demographics_router


def register_routers(app):
    app.register_blueprint(kpi_router, url_prefix="/api")
    app.register_blueprint(tourists_router, url_prefix="/api")
    app.register_blueprint(regions_router, url_prefix="/api")
    app.register_blueprint(demographics_router, url_prefix="/api")
