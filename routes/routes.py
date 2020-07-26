# Retic
from retic import Router

# Controllers
import controllers.cache as cache

"""Define Router instance"""
router = Router()

"""Define all routes - /downloads/files"""
router \
    .get("/downloads/files/:file", cache.get_by_id)

"""Define all routes - /cache/files"""
router \
    .delete("/cache/files", cache.clean_cache_files)
