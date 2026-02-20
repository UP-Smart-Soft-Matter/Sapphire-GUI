import logging
import coloredlogs

log_level = logging.DEBUG
logging.basicConfig(level=log_level)

logger = logging.getLogger(__name__)

field_styles = {
    'asctime': {'color': 'white'},
    'levelname': {'color': 'blue', 'bold': True},
}
coloredlogs.install(
    level=log_level,
    logger=logger,
    fmt='%(asctime)s - %(levelname)s - %(message)s',
    field_styles=field_styles)

