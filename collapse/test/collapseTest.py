from unittest import TestCase
import collapse.collapse as c

class CollapseTest(TestCase):

    # 100 collapse
    #    Desired level of confidence:    boundary value analysis
    #    Input-output Analysis
    #      inputs: value -> numeric; .GE. 0 and .LT. 100; mandatory, unvalidated
    #      outputs: 
    #         normal:  single digit string
    #         abnormal: None
    #         side effects:  none
    
    
    #  Sample happy path test -- replace with your own
    def test100_010ShouldCalculateNominalInput(self):
        value = '9'
        expectedResult = '9'
        actualResult = c.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    #  Sample sad path test -- replace with your own
    def test100_910ShouldDetectBadInput(self):
        value = 'a'
        expectedResult = None
        actualResult = c.collapse(value)
        self.assertEqual(expectedResult, actualResult)
    
    
