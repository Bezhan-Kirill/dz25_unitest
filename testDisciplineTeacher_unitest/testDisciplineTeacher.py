import unittest
from classDisciplineTeacher import DisciplineTeacher


class TestDisciplineTeacher(unittest.TestCase):
    disciplineteacher = DisciplineTeacher('test_name', 'test_education', 'test_experience', 'test_discipline',
                                          'test_job_title')

    def test_1_init(self):
        self.assertEqual(len(DisciplineTeacher.teachers_list), 0)

    def test_2_get_name(self):
        self.assertEqual(self.disciplineteacher.get_name(), "test_name")

    def test_3_get_education(self):
        self.assertEqual(self.disciplineteacher.get_education(), "test_education")

    def test_4_get_experience(self):
        self.assertEqual(self.disciplineteacher.get_experience(), "test_experience")

    def test_5_get_discipline(self):
        self.assertEqual(self.disciplineteacher.get_discipline(), "test_discipline")

    def test_6_get_job_title(self):
        self.assertEqual(self.disciplineteacher.get_job_title(), "test_job_title")

    def test_7_add_mark(self):
        self.assertEqual(self.disciplineteacher.add_mark("Иван Иванов", "5"), "Предмет: test_discipline")

    def test_8_remove_mark(self):
        self.assertEqual(self.disciplineteacher.remove_mark("Иван Иванов", "5"), "Предмет: test_discipline")

    def test_9_get_a_consultation(self):
        self.assertEqual(self.disciplineteacher.give_a_consultation("9Б"),
                         "По прeдмету test_discipline как test_job_title")

    def test_10_fire_teacher(self):
        self.assertEqual(self.disciplineteacher.fire_teacher(), "Учитель был уволен!")
        self.assertEqual(self.disciplineteacher.fire_teacher(), "Этот учитель уже был уволен!")

    def test_11_get_teacher_data(self):
        self.assertEqual(self.disciplineteacher.get_teacher_data(),
                         "Предмет: test_discipline, должность test_job_title")

    def test_12_set_job_title(self):
        self.assertEqual(self.disciplineteacher.set_job_title("test_job_title"), None)
