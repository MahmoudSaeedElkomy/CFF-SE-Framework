"""
Configuration settings for the Cognitive Fortress Framework.
"""

# Framework Configuration
FRAMEWORK_CONFIG = {
    "default_sensitivity": "medium",
    "enable_logging": True,
    "log_level": "INFO",
    "max_analysis_depth": 3,
    "response_timeout": 30,  # seconds
}

# Module-Specific Configurations
MODULE_CONFIGS = {
    "awareness": {
        "sensitivity_threshold": 0.5,
        "trigger_weighting": {
            "emotional_language": 1.0,
            "authority_bias": 0.8,
            "scarcity_priming": 0.7,
            "social_proof_manipulation": 0.6,
            "reciprocity_pressure": 0.5
        }
    },
    "critical_thinking": {
        "min_evaluation_score": 25,
        "analysis_techniques": [
            "question_assumptions",
            "evaluate_evidence",
            "consider_alternatives",
            "check_logic",
            "identify_bias"
        ]
    },
    "bias_detector": {
        "bias_threshold": 0.6,
        "known_biases": [
            "confirmation_bias",
            "anchoring_bias",
            "availability_heuristic",
            "authority_bias",
            "bandwagon_effect",
            "framing_effect",
            "hindsight_bias",
            "overconfidence_effect"
        ]
    }
}

# Security Settings
SECURITY_CONFIG = {
    "encryption_enabled": True,
    "data_retention_days": 30,
    "audit_logging": True,
    "anonymization_level": "high"
}

# Performance Settings
PERFORMANCE_CONFIG = {
    "cache_enabled": True,
    "max_cache_size": 1000,
    "parallel_processing": True,
    "thread_limit": 10
}

# User Interface Settings
UI_CONFIG = {
    "theme": "dark",
    "language": "en",
    "show_advanced_options": False,
    "auto_update_notifications": True
}


def get_config(module_name=None):
    """
    Retrieve configuration settings.
    
    Args:
        module_name (str, optional): Name of the module to get config for
        
    Returns:
        dict: Configuration settings
    """
    if module_name and module_name in MODULE_CONFIGS:
        return {
            **FRAMEWORK_CONFIG,
            **MODULE_CONFIGS[module_name],
            **SECURITY_CONFIG,
            **PERFORMANCE_CONFIG
        }
    
    # Return all configurations combined
    config = {**FRAMEWORK_CONFIG}
    for module_config in MODULE_CONFIGS.values():
        config.update(module_config)
    config.update(SECURITY_CONFIG)
    config.update(PERFORMANCE_CONFIG)
    config.update(UI_CONFIG)
    
    return config


def update_config(new_settings):
    """
    Update configuration settings.
    
    Args:
        new_settings (dict): New settings to update
    """
    global FRAMEWORK_CONFIG, MODULE_CONFIGS, SECURITY_CONFIG, PERFORMANCE_CONFIG, UI_CONFIG
    
    for key, value in new_settings.items():
        if key in FRAMEWORK_CONFIG:
            FRAMEWORK_CONFIG[key] = value
        elif key in MODULE_CONFIGS:
            MODULE_CONFIGS[key].update(value)
        elif key in SECURITY_CONFIG:
            SECURITY_CONFIG[key] = value
        elif key in PERFORMANCE_CONFIG:
            PERFORMANCE_CONFIG[key] = value
        elif key in UI_CONFIG:
            UI_CONFIG[key] = value