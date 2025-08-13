# Web UI Test Framework - Weather

## Install Dependencies
安装所需依赖并初始化 Playwright 浏览器：
```bash
pip install -r requirements.txt
python -m playwright install
```

## Run All Test Cases
运行 tests 目录下的所有测试：
```bash
python -m pytest tests
```

## Run a Specific Test Suite
运行某一个测试文件（测试套件）：
```bash
python -m pytest tests/test_search_city_spec.py
```

## Run a Specific Test Case in a Suite
运行某个测试套件中的单个测试方法（假设方法名为 test_search_city）：
```bash
python -m pytest tests/test_search_city_spec.py::test_search_city
```

## Run Tests With Verbose Output
以详细模式运行（显示每个测试的执行过程）：
```bash
python -m pytest -v tests
```

## Tips
所有命令都需在项目根目录（web-ui-test-framework）下执行。

如果出现 ModuleNotFoundError: No module named 'controllers' 之类错误，可尝试：
```bash
# Windows
set PYTHONPATH=%CD%

# Linux / Mac
export PYTHONPATH=$(pwd)
```
然后重新运行测试。

调试时推荐使用 VS Code 的 launch.json 配置，直接 F5 运行或断点调试。
```bash

---

### **VS Code 调试配置 `.vscode/launch.json`**
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Pytest - Run All Tests",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": [
                "tests"
            ],
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        },
        {
            "name": "Pytest - Run Current Test File",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": [
                "${file}"
            ],
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        },
        {
            "name": "Pytest - Run Single Test Function",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": [
                "${file}::${selectedText}"
            ],
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        }
    ]
}
```

## 说明

Run All Tests → 运行 tests 下所有用例

Run Current Test File → 运行当前打开的测试文件

Run Single Test Function → 选中函数名后运行该用例