# nothing there yet
from src.utils.utils import HelperUtils

"""
The simple integration test class, This class can be used to do the unit testing with the function written in transform class.
The possible unit testing in current scenario:
1. Test if the windows interval is 10 minutes
2. Test if the read schema is correct
3. Test if the avg no of actions are correct
4. Test if the total action type is correct

We can check each transformation job separately just like normal python unit test. With spark it can be trickier as the job may 
have relation with external sources and sinks
"""

class TestTransformationJobs:

    pass