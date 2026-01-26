"""
Main entry point for the Cognitive Fortress Framework.
"""

from core.framework import CognitiveFortressFramework
from modules.awareness import AwarenessModule, RealityCheckModule
from modules.critical_thinking import CriticalThinkingModule, BiasDetectorModule
from utils.helpers import format_report
from config.settings import get_config


def main():
    """Main function to demonstrate the Cognitive Fortress Framework."""
    print("Initializing Cognitive Fortress Framework...")
    
    # Create the main framework instance
    cff = CognitiveFortressFramework()
    
    # Configure the framework
    cff.config = get_config()
    
    # Register defense modules
    cff.register_module("awareness", AwarenessModule())
    cff.register_module("reality_check", RealityCheckModule())
    cff.register_module("critical_thinking", CriticalThinkingModule())
    cff.register_module("bias_detection", BiasDetectorModule())
    
    # Activate the framework
    cff.activate()
    
    # Example inputs to analyze
    test_inputs = [
        "URGENT: Limited time offer! Act now before it's too late!",
        "According to leading experts, this is the best solution available.",
        "This is a factual statement without manipulation."
    ]
    
    print("\nAnalyzing inputs with Cognitive Fortress Framework...\n")
    
    for i, input_text in enumerate(test_inputs, 1):
        print(f"Input {i}: {input_text}")
        
        # Apply all defenses to the input
        results = cff.apply_defenses(input_text)
        
        # Print formatted reports for each module
        for module_name, module_result in results.items():
            print(f"\n[{module_name.upper()} REPORT]")
            print(format_report(module_result))
        print("\n" + "-"*50 + "\n")
    
    # Deactivate the framework
    cff.deactivate()
    print("Cognitive Fortress Framework deactivated.")


if __name__ == "__main__":
    main()