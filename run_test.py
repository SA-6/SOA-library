import unittest
import os
import sys
import argparse

# 将项目根目录添加到系统路径中，以便能够导入 app 和其他模块
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

def main():
    parser = argparse.ArgumentParser(description='Run specific test files and/or functions.')
    parser.add_argument('test_files', nargs='*', help='List of test files to run (e.g., test_app.py test_users.py)')
    parser.add_argument('--function', '-f', help='Specific function to run within the test files')
    args = parser.parse_args()

    if args.test_files:
        # 如果指定了测试文件，则只运行这些文件
        test_loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        for test_file in args.test_files:
            test_module = f'test.{os.path.splitext(test_file)[0]}.TestApp'
            try:
                if args.function:
                    # 如果指定了测试函数，则只运行该函数
                    test_name = f'{test_module}.{args.function}'
                    suite.addTests(test_loader.loadTestsFromName(test_name))
                else:
                    # 否则运行整个模块的所有测试用例
                    module = __import__(test_module, fromlist=['*'])
                    suite.addTests(test_loader.loadTestsFromModule(module))
            except (ImportError, AttributeError) as e:
                print(f"Error loading test file or function {test_file}: {e}")
    else:
        # 如果未指定测试文件，则发现并运行 tests 文件夹下的所有测试用例
        suite = test_loader.discover(os.path.join(project_root, 'test'))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main()