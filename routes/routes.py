# Retic
from retic import Router
from retic.lib.hooks.middlewares import cors

# Controllers
import controllers.cache as cache

"""Define Router instance"""
router = Router()

"""Define CORS"""
_cors = cors(
    headers="Content-Type,source",
    expose_headers="Content-Type,source"
)

"""Add cors settigns"""
router.use(_cors)

"""Define the options methods for all routes"""
router.options("/*", _cors)

"""Define all routes - /downloads/files"""
router \
    .get("/downloads/files/:file", cache.get_by_id)

"""Define all routes - /cache/files"""
router \
    .delete("/cache/files", cache.clean_cache_files)
