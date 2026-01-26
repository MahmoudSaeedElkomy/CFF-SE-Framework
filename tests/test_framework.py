"""
Test suite for the Cognitive Fortress Framework.
"""

import unittest
from core.framework import CognitiveFortressFramework, DefenseModule
from modules.awareness import AwarenessModule, RealityCheckModule
from modules.critical_thinking import CriticalThinkingModule, BiasDetectorModule


class TestCognitiveFortressFramework(unittest.TestCase):
    """Test cases for the main framework."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.framework = CognitiveFortressFramework()
        
    def test_framework_initialization(self):
        """Test that the framework initializes correctly."""
        self.assertEqual(self.framework.status, "inactive")
        self.assertEqual(self.framework.modules, {})
        self.assertEqual(self.framework.defense_layers, [])
        
    def test_framework_activation(self):
        """Test activating and deactivating the framework."""
        self.framework.activate()
        self.assertEqual(self.framework.status, "active")
        
        self.framework.deactivate()
        self.assertEqual(self.framework.status, "inactive")
        
    def test_module_registration(self):
        """Test registering modules with the framework."""
        mock_module = MockModule("Test Module")
        self.framework.register_module("test", mock_module)
        
        self.assertIn("test", self.framework.modules)
        self.assertEqual(self.framework.modules["test"], mock_module)
        
    def test_threat_assessment(self):
        """Test threat assessment functionality."""
        result = self.framework.assess_threat("sample input")
        self.assertIn("threat_level", result)
        self.assertIn("details", result)
        

class TestAwarenessModule(unittest.TestCase):
    """Test cases for the Awareness Module."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.module = AwarenessModule()
        
    def test_module_initialization(self):
        """Test that the awareness module initializes correctly."""
        self.assertEqual(self.module.name, "Awareness Module")
        self.assertIsNotNone(self.module.triggers)
        
    def test_process_with_triggers(self):
        """Test processing input that contains trigger words."""
        input_with_triggers = "This is an urgent crisis that requires immediate action!"
        result = self.module.process(input_with_triggers)
        
        self.assertGreater(len(result["triggers_detected"]), 0)
        self.assertGreater(result["awareness_score"], 0)
        self.assertGreater(len(result["recommendations"]), 0)
        
    def test_process_without_triggers(self):
        """Test processing input without trigger words."""
        input_without_triggers = "This is a neutral statement about weather."
        result = self.module.process(input_without_triggers)
        
        self.assertEqual(len(result["triggers_detected"]), 0)
        self.assertEqual(result["awareness_score"], 0)
        self.assertGreater(len(result["recommendations"]), 0)
        

class TestCriticalThinkingModule(unittest.TestCase):
    """Test cases for the Critical Thinking Module."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.module = CriticalThinkingModule()
        
    def test_module_initialization(self):
        """Test that the critical thinking module initializes correctly."""
        self.assertEqual(self.module.name, "Critical Thinking Module")
        self.assertIsNotNone(self.module.analysis_techniques)
        
    def test_process_short_input(self):
        """Test processing short input."""
        short_input = "Yes"
        result = self.module.process(short_input)
        
        self.assertEqual(result["evaluation_score"], 25)
        self.assertGreater(len(result["critical_questions"]), 0)
        
    def test_process_long_input(self):
        """Test processing longer input."""
        long_input = "This is a much longer input that should receive a higher evaluation score based on its length and complexity."
        result = self.module.process(long_input)
        
        self.assertGreaterEqual(result["evaluation_score"], 50)
        self.assertGreater(len(result["critical_questions"]), 0)
        

class TestBiasDetectorModule(unittest.TestCase):
    """Test cases for the Bias Detector Module."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.module = BiasDetectorModule()
        
    def test_module_initialization(self):
        """Test that the bias detector module initializes correctly."""
        self.assertEqual(self.module.name, "Bias Detector Module")
        self.assertIsNotNone(self.module.known_biases)
        
    def test_process_with_biases(self):
        """Test processing input that contains bias-indicating words."""
        input_with_bias = "As the expert says, this is the best product ever. Everyone is buying it now!"
        result = self.module.process(input_with_bias)
        
        self.assertGreater(len(result["biases_detected"]), 0)
        self.assertGreater(result["bias_score"], 0)
        self.assertGreater(len(result["mitigation_strategies"]), 0)
        

class MockModule(DefenseModule):
    """Mock module for testing purposes."""
    
    def process(self, input_data):
        return input_data


def run_tests():
    """Run all tests in the test suite."""
    unittest.main()


if __name__ == "__main__":
    run_tests()