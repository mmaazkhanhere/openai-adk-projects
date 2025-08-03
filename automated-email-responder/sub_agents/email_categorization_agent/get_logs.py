import logging
import sys
from datetime import datetime
from typing import Optional
import os
from logging.handlers import TimedRotatingFileHandler

class AppLogger:
    def __init__(self, name: str = "app", log_dir: str = "logs"):
        """
        Initialize a readable logger for the entire application
        
        Args:
            name: Logger name (usually __name__)
            log_dir: Directory to store log files
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)  # Capture all levels
        
        # Create log directory if needed
        os.makedirs(log_dir, exist_ok=True)
        
        # Custom formatters
        console_formatter = ColoredFormatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        file_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        # Console handler (stderr)
        console_handler = logging.StreamHandler(sys.stderr)
        console_handler.setLevel(logging.INFO)  # Only show INFO+ in console
        console_handler.setFormatter(console_formatter)
        
        # Debug file handler (all levels)
        debug_handler = TimedRotatingFileHandler(
            filename=f"{log_dir}/debug.log",
            when="midnight",
            backupCount=7
        )
        debug_handler.setLevel(logging.DEBUG)
        debug_handler.setFormatter(file_formatter)
        
        # Error file handler (errors only)
        error_handler = TimedRotatingFileHandler(
            filename=f"{log_dir}/error.log",
            when="midnight",
            backupCount=7
        )
        error_handler.setLevel(logging.WARNING)
        error_handler.setFormatter(file_formatter)
        
        # Add handlers
        self.logger.addHandler(console_handler)
        self.logger.addHandler(debug_handler)
        self.logger.addHandler(error_handler)
        
    def section(self, title: str, level: str = "DEBUG"):
        """Log a visible section header"""
        msg = f"\n╔{'═' * (len(title) + 2)}╗\n║ {title.upper()} ║\n╚{'═' * (len(title) + 2)}╝"
        getattr(self.logger, level.lower())(msg)
    
    def debug(self, msg: str, **kwargs):
        self.logger.debug(msg, **kwargs)
        
    def info(self, msg: str, **kwargs):
        self.logger.info(msg, **kwargs)
        
    def warning(self, msg: str, **kwargs):
        self.logger.warning(msg, **kwargs)
        
    def error(self, msg: str, exc_info: Optional[bool] = None, **kwargs):
        self.logger.error(msg, exc_info=exc_info, **kwargs)
        
    def critical(self, msg: str, **kwargs):
        self.logger.critical(msg, **kwargs)

class ColoredFormatter(logging.Formatter):
    """Add color to console logs for better readability"""
    COLORS = {
        'DEBUG': '\033[36m',    # Cyan
        'INFO': '\033[32m',     # Green
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',    # Red
        'CRITICAL': '\033[41m'  # Red background
    }
    RESET = '\033[0m'
    
    def format(self, record):
        level_color = self.COLORS.get(record.levelname, '')
        record.levelname = f"{level_color}{record.levelname}{self.RESET}"
        return super().format(record)

# Global logger instance
logger = AppLogger("app")