"""
Awareness and Recognition Module for the Cognitive Fortress Framework.
"""

from core.framework import DefenseModule


class AwarenessModule(DefenseModule):
    """
    Module responsible for increasing awareness and recognition of cognitive manipulation attempts.
    """
    
    def __init__(self):
        super().__init__(
            name="Awareness Module",
            description="Increases awareness and recognition of cognitive manipulation attempts."
        )
        self.triggers = [
            "emotional_language",
            "authority_bias",
            "scarcity_priming",
            "social_proof_manipulation",
            "reciprocity_pressure"
        ]
        
    def process(self, input_data):
        """
        Process input data to increase awareness of potential manipulation attempts.
        
        Args:
            input_data: The input to analyze for manipulation triggers
            
        Returns:
            dict: Processed data with awareness indicators
        """
        awareness_report = {
            "input": input_data,
            "triggers_detected": [],
            "awareness_score": 0,
            "recommendations": []
        }
        
        # Simple pattern matching for trigger words/phrases
        input_lower = str(input_data).lower()
        
        for trigger in self.triggers:
            trigger_words = {
                "emotional_language": ["urgent", "crisis", "desperate", "fear"],
                "authority_bias": ["expert", "doctor", "professor", "official", "study shows"],
                "scarcity_priming": ["limited time", "only few left", "deadline", "act now"],
                "social_proof_manipulation": ["everyone", "thousands", "best-selling", "popular"],
                "reciprocity_pressure": ["free gift", "complimentary", "as a thank you"]
            }
            
            if trigger in trigger_words:
                for word in trigger_words[trigger]:
                    if word in input_lower:
                        awareness_report["triggers_detected"].append({
                            "type": trigger,
                            "word_found": word,
                            "confidence": "medium"
                        })
        
        # Calculate awareness score based on triggers detected
        awareness_report["awareness_score"] = min(len(awareness_report["triggers_detected"]) * 20, 100)
        
        # Generate recommendations based on triggers found
        if awareness_report["triggers_detected"]:
            awareness_report["recommendations"].append(
                "Be cautious of potential cognitive biases and manipulation attempts."
            )
            awareness_report["recommendations"].append(
                "Consider taking a step back to evaluate the information objectively."
            )
        else:
            awareness_report["recommendations"].append(
                "No obvious manipulation triggers detected. Continue to think critically."
            )
        
        return awareness_report


class RealityCheckModule(DefenseModule):
    """
    Module that implements reality-checking techniques to verify information validity.
    """
    
    def __init__(self):
        super().__init__(
            name="Reality Check Module",
            description="Implements reality-checking techniques to verify information validity."
        )
        
    def process(self, input_data):
        """
        Apply reality-checking techniques to the input data.
        
        Args:
            input_data: The input to verify
            
        Returns:
            dict: Processed data with verification results
        """
        verification_result = {
            "input": input_data,
            "fact_check_status": "pending",
            "source_credibility": "unknown",
            "logical_consistency": "unknown",
            "verification_steps": []
        }
        
        # Add verification steps
        verification_result["verification_steps"].extend([
            "Verify claims with independent sources",
            "Check publication date and context",
            "Look for evidence supporting claims",
            "Consider alternative explanations",
            "Evaluate source credentials and potential bias"
        ])
        
        # Set default status
        verification_result["fact_check_status"] = "recommended"
        verification_result["logical_consistency"] = "to_be_evaluated"
        
        return verification_result