import unittest
from classTeacher import Teacher


class TestTeacher(unittest.TestCase):
    teacher = Teacher('test_name', 'test_education', 'test_experience')

    def test_1_get_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(), "test_name, test_education, опыт работы test_experience")

    def test_2_add_mark(self):
        self.assertEqual(self.teacher.add_mark("test_student", "test_grade"),
                         "test_name поставил оценку test_grade студенту test_student")

    def test_3_add_mark(self):
        self.assertEqual(self.teacher.remove_mark("test_student", "test_grade"),
                         "test_name удалил оценку test_grade студенту test_student")

    def test_4_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation("test_classroom"),
                         "test_name провел консультацию в кабинете test_classroom")

    def test_5_get_name(self):
        self.assertEqual(self.teacher.get_name(), "test_name")

    def test_6_get_education(self):
        self.assertEqual(self.teacher.get_education(), "test_education")

    def test_7_get_experience(self):
        self.assertEqual(self.teacher.get_experience(), "test_experience")

    def test_8_set_experience(self):
        self.assertEqual(self.teacher.set_experience("test_experienc"), None)
