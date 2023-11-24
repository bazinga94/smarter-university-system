from datetime import datetime
import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):

        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        specific_datetime = datetime(2023, 11, 23, 12, 30, 0)  # Nov 23, 2023, at 12:30:00
        specific_datetime2 = datetime(2023, 12, 23, 12, 30, 0)  # Dec 23, 2023, at 12:30:00
        quiz_id = self.ctrl.add_quiz("q1",'test',specific_datetime,specific_datetime2)
        q = self.ctrl.get_quiz_by_id(quiz_id)
        self.assertIsNotNone(q, 'Get None quiz.')

        self.ctrl.add_quiz(None, "Sample Text", datetime.now(), datetime.now())
        ''' 
        crash info:
        File "app/controllers/quizzes_controller.py", line 63, in add_quiz
        quiz_id = utils.generate_id(title + updated_date.isoformat())
    TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
        '''                
    
    def test_expose_failure_02(self):
        """
        A test that induces a crash by attempting to retrieve a quiz with a corrupted(NoneType) data.
        """
        # Clear quiz data if any is present
        self.ctrl.clear_data()

        # Simulate data corruption
        self.ctrl.quizzes = None

        # Trigger crash by attempting to retrieve a corrupted data
        quiz = self.ctrl.get_quiz_by_id("sample_id")

        # Assert that the program has not crashed
        quizzes = self.ctrl.get_quizzes()
        self.assertEqual(len(quizzes), 0, "Number of quizzes should be 0.")

        ''' 
        crash info:
        "smarter-university-system/app/controllers/quizzes_controller.py", line 117, in get_quiz_by_id
        quizzes = [q for q in self.quizzes if q.id == quiz_id]
        TypeError: 'NoneType' object is not iterable
        '''
        
    def test_expose_failure_03(self):

        
        fileName=None
        self.ctrl = QuizzesController(fileName)
        self.ctrl.clear_data()
        specific_datetime = datetime(2023, 11, 23, 12, 30, 0)  # Nov 23, 2023, at 12:30:00
        specific_datetime2 = datetime(2023, 12, 23, 12, 30, 0)  # Dec 23, 2023, at 12:30:00
        quiz_id = self.ctrl.add_quiz("q2",'test',specific_datetime,specific_datetime2)
        q = self.ctrl.get_quiz_by_id(quiz_id)
        self.assertEqual(len(q), 1, 'testing')

        ''' 
        crash info:
        TypeError: join() argument must be str, bytes, or os.PathLike object, not 'NoneType'
        
        '''     

if __name__ == '__main__':
    unittest.main()
