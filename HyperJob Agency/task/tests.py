from hstest import dynamic_test

from test.base import HyperJobTest


class HyperJobTestRunner(HyperJobTest):

    funcs = [
        # 1 task
        HyperJobTest.check_create_vacancies,
        HyperJobTest.check_create_resumes,
        # 2 task
        HyperJobTest.check_greeting,
        HyperJobTest.check_links,
        # 3 task
        HyperJobTest.check_vacancies,
        HyperJobTest.check_resumes,
    ]

    @dynamic_test(data=funcs)
    def test(self, func):
        return func(self)


if __name__ == '__main__':
    HyperJobTestRunner().run_tests()
