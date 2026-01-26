"""
Helper utilities for the Cognitive Fortress Framework.
"""


def calculate_confidence_score(detection_results):
    """
    Calculate an overall confidence score based on detection results.
    
    Args:
        detection_results: Dictionary containing detection results from various modules
        
    Returns:
        float: Confidence score between 0 and 100
    """
    if not detection_results:
        return 0
    
    scores = []
    if 'awareness_score' in detection_results:
        scores.append(detection_results['awareness_score'])
    if 'evaluation_score' in detection_results:
        scores.append(detection_results['evaluation_score'])
    if 'bias_score' in detection_results:
        scores.append(detection_results['bias_score'])
    
    if not scores:
        return 0
    
    return sum(scores) / len(scores)


def normalize_text(text):
    """
    Normalize text for consistent processing.
    
    Args:
        text: Input text to normalize
        
    Returns:
        str: Normalized text
    """
    if not isinstance(text, str):
        text = str(text)
    
    # Convert to lowercase and strip whitespace
    normalized = text.lower().strip()
    
    # Remove extra whitespace
    normalized = ' '.join(normalized.split())
    
    return normalized


def format_report(results):
    """
    Format analysis results into a readable report.
    
    Args:
        results: Dictionary containing analysis results
        
    Returns:
        str: Formatted report
    """
    report_lines = ["Cognitive Fortress Analysis Report", "="*35]
    
    for key, value in results.items():
        if isinstance(value, list) and value:
            report_lines.append(f"\n{key.replace('_', ' ').title()}:")
            if isinstance(value[0], dict):
                for item in value:
                    for sub_key, sub_value in item.items():
                        report_lines.append(f"  - {sub_key}: {sub_value}")
            else:
                for item in value:
                    report_lines.append(f"  - {item}")
        elif not isinstance(value, (dict, list)):
            report_lines.append(f"{key.replace('_', ' ').title()}: {value}")
    
    return "\n".join(report_lines)


def merge_results(*result_dicts):
    """
    Merge multiple result dictionaries into a single dictionary.
    
    Args:
        *result_dicts: Variable number of result dictionaries to merge
        
    Returns:
        dict: Merged results dictionary
    """
    merged = {}
    
    for result_dict in result_dicts:
        for key, value in result_dict.items():
            if key in merged:
                # If both values are lists, extend them
                if isinstance(merged[key], list) and isinstance(value, list):
                    merged[key].extend(value)
                # If both values are numbers, add them
                elif isinstance(merged[key], (int, float)) and isinstance(value, (int, float)):
                    merged[key] += value
                # Otherwise, keep the first value or convert to list
                else:
                    if not isinstance(merged[key], list):
                        merged[key] = [merged[key]]
                    merged[key].append(value)
            else:
                merged[key] = value
                
    return merged


def is_valid_input(input_data):
    """
    Validate if the input is suitable for analysis.
    
    Args:
        input_data: Input to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if input_data is None:
        return False
    
    if isinstance(input_data, str):
        return len(input_data.strip()) > 0
    
    if isinstance(input_data, (list, tuple)):
        return len(input_data) > 0
    
    return True