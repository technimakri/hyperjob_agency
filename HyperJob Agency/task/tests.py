from hstest import dynamic_test

from test.base import HyperJobTest


class HyperJobTestRunner(HyperJobTest):

    funcs = [
        HyperJobTest.check_create_vacancies,
        HyperJobTest.check_create_resumes
    ]

    @dynamic_test(data=funcs)
    def test(self, func):
        return func(self)


if __name__ == '__main__':
    HyperJobTestRunner().run_tests()
