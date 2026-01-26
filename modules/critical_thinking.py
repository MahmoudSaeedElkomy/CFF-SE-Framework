"""
Critical Thinking Module for the Cognitive Fortress Framework.
"""

from core.framework import DefenseModule


class CriticalThinkingModule(DefenseModule):
    """
    Module that enhances critical thinking capabilities to analyze information effectively.
    """
    
    def __init__(self):
        super().__init__(
            name="Critical Thinking Module",
            description="Enhances critical thinking capabilities to analyze information effectively."
        )
        self.analysis_techniques = [
            "question_assumptions",
            "evaluate_evidence",
            "consider_alternatives",
            "check_logic",
            "identify_bias"
        ]
        
    def process(self, input_data):
        """
        Apply critical thinking techniques to analyze the input data.
        
        Args:
            input_data: The input to analyze critically
            
        Returns:
            dict: Analysis results with critical thinking insights
        """
        analysis_result = {
            "input": input_data,
            "analysis_summary": "",
            "critical_questions": [],
            "evaluation_score": 0,
            "techniques_applied": []
        }
        
        # Generate critical questions to ask about the input
        analysis_result["critical_questions"] = [
            "What evidence supports this claim?",
            "Are there alternative explanations?",
            "Who is the source and what are their credentials?",
            "What might be the motivations behind this information?",
            "Is there any logical fallacy in the reasoning?",
            "How does this align with known facts?",
            "What would happen if this information is incorrect?"
        ]
        
        # Determine evaluation score based on complexity of input
        input_str = str(input_data)
        if len(input_str) > 100:
            analysis_result["evaluation_score"] = 75
        elif len(input_str) > 50:
            analysis_result["evaluation_score"] = 50
        else:
            analysis_result["evaluation_score"] = 25
            
        analysis_result["techniques_applied"] = self.analysis_techniques
        
        analysis_result["analysis_summary"] = (
            f"Applied {len(self.analysis_techniques)} critical thinking techniques "
            f"to analyze the input. Generated {len(analysis_result['critical_questions'])} "
            f"critical questions for deeper evaluation."
        )
        
        return analysis_result


class BiasDetectorModule(DefenseModule):
    """
    Module that identifies and highlights potential cognitive biases in information.
    """
    
    def __init__(self):
        super().__init__(
            name="Bias Detector Module",
            description="Identifies and highlights potential cognitive biases in information."
        )
        self.known_biases = [
            "confirmation_bias",
            "anchoring_bias",
            "availability_heuristic",
            "authority_bias",
            "bandwagon_effect",
            "framing_effect",
            "hindsight_bias",
            "overconfidence_effect"
        ]
        
    def process(self, input_data):
        """
        Detect potential cognitive biases in the input data.
        
        Args:
            input_data: The input to analyze for biases
            
        Returns:
            dict: Bias detection results
        """
        bias_detection = {
            "input": input_data,
            "biases_detected": [],
            "bias_score": 0,
            "mitigation_strategies": []
        }
        
        # Simple keyword-based bias detection
        input_lower = str(input_data).lower()
        
        bias_keywords = {
            "confirmation_bias": ["only listen to", "everyone agrees", "proves me right"],
            "anchoring_bias": ["first impression", "initial price", "starting point"],
            "authority_bias": ["expert says", "doctor recommends", "studies show"],
            "bandwagon_effect": ["everyone is doing", "most people", "trending now"],
            "framing_effect": ["loss of", "gain of", "only $X per day"]
        }
        
        detected_biases = []
        for bias, keywords in bias_keywords.items():
            for keyword in keywords:
                if keyword in input_lower:
                    detected_biases.append({
                        "type": bias,
                        "keyword_found": keyword,
                        "severity": "medium"
                    })
                    
        bias_detection["biases_detected"] = detected_biases
        bias_detection["bias_score"] = min(len(detected_biases) * 25, 100)
        
        # Add mitigation strategies
        bias_detection["mitigation_strategies"] = [
            "Seek out diverse perspectives and opinions",
            "Question your initial reactions and assumptions",
            "Look for disconfirming evidence",
            "Consider the opposite viewpoint",
            "Evaluate the source's credibility and potential bias",
            "Take time to reflect before making decisions"
        ]
        
        return bias_detection